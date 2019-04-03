config = {}

config["HOST_NAME"] = ''
config["BIND_PORT"] = 5000
config["MAX_REQUEST_LEN"] = 8191 * 2 + 1
config['CONNECTION_TIMEOUT'] = 10

config["403"] = """\
HTTP/1.1 403 Unauthorized
Content-Type text/html

<p>403 Forbidden</p>
""".encode()

config["404"] = """\
HTTP/1.1 404 Not Found
Content-Type text/html

{}\
"""
