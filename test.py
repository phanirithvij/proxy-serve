import socket
import os
import sys

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(6)

print(f'Serving HTTP on port {PORT} ...')
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(2048)
    request = request.decode('utf-8').split(os.linesep)
    print(request)
    method = request[0].split(' ')[0]
    path = request[0].split(' ')[1]
    print(method, path)

    http_response = """\
HTTP/1.1 200 OK
Content-Type : text/html

<p>Hello, World!</p>
<h1>Good god</h1>
"""
    client_connection.sendall(http_response.encode())
    client_connection.close()
