import signal, sys
import socket
import threading
from config import config
from cacher import do_caching_or_request
from utils import get_black_list


class Server:
    def __init__(self, config):
        # Shutdown on Ctrl+C
        signal.signal(signal.SIGINT, self.shutdown)

        self.config = config

        # Create a TCP socket
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Re-use the socket
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind the socket to a public host, and a port 
        self.serverSocket.bind((config['HOST_NAME'], config['BIND_PORT']))

        self.serverSocket.listen(100) # become a server socket
        self._clients = []
        self.blocked = get_black_list()

    def shutdown(self, signum, frame):
        """ Handle the exiting server. Clean all traces """
        main_thread = threading.currentThread() # Wait for all clients to exit
        for t in threading.enumerate():
            if t is main_thread:
                print("FAIL", -1, 'joining ' + t.getName())
                continue
            t.join()
            self.serverSocket.close()
        sys.exit(0)

    def proxy_thread(self, clientSocket, client_address):
        # get the request from browser
        request = clientSocket.recv(config['MAX_REQUEST_LEN'])

        self._clients.append(clientSocket)

        print(request.decode('utf-8'))

        # parse the first line
        first_line = request.decode('utf-8').split('\n')[0]

        print("first line", first_line)

        # get url
        url = first_line.split(' ')[1]

        http_pos = url.find("://") # find pos of ://
        if (http_pos==-1):
            temp = url
        else:
            temp = url[(http_pos+3):] # get the rest of url

        port_pos = temp.find(":") # find the port pos (if any)

        # find end of web server
        webserver_pos = temp.find("/")
        if webserver_pos == -1:
            webserver_pos = len(temp)

        webserver = ""
        port = -1
        if (port_pos==-1 or webserver_pos < port_pos):
            # default port
            port = 80
            webserver = temp[:webserver_pos]

        else: # specific port
            port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
            webserver = temp[:port_pos]
    
        print(f"trying to request {webserver}:{port}")
        print(webserver)

        if port == 443:
            print("No https")
            return

        urlip = socket.gethostbyname(webserver)   
        print("HOST ",socket.gethostbyname(webserver))
        
        if urlip in self.blocked :
            clientSocket.send(b"""\
                HTTP/1.0 403 Unauthorized
                Content-Type text/html
                
                Forbidden"""
            ) # send to browser/client
            
            print ('lsi is blocked')
        else :
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            s.settimeout(config['CONNECTION_TIMEOUT'])
            try:
                s.connect((webserver, port))
            except ConnectionRefusedError as _e:
                print("refused ", _e)
                clientSocket.send("""\
                    HTTP/1.0 404 Not Found
                    Content-Type text/html

                    {}\
                    """.format(str(_e)).encode()
                ) # send to browser/client

                return

            s.sendall(request)
            while True:
                # receive data from web server
                data = s.recv(config['MAX_REQUEST_LEN'])
                print("while true")
                if (len(data) > 0):
                    print('sending to client', data)
                    clientSocket.send(data) # send to browser/client
                else:
                    break


    def run(self):
        print(f"starting the server on {self.config['BIND_PORT']}...")
        while True:
            # Establish the connection
            (clientSocket, client_address) = self.serverSocket.accept()
            print('new request', client_address)

            d = threading.Thread(
                name=self._getClientName(client_address),
                target = self.proxy_thread,
                args=(clientSocket, client_address)
            )
            d.setDaemon(True)
            d.start()

    def _getClientName(self, cadd):
        return f'th-{cadd[1]}'

if __name__ == "__main__":
    server = Server(config)
    server.run()
