import socket

port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", port))
server.listen(1)
print(f"Listening on port {port}...")

conn, addr = server.accept()
print(f"Connection received from {addr}")
conn.close()
