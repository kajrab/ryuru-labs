import socket

s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind(("127.0.0.2", 6573))

s_socket.listen(1)
print("Server is listening...")

conn, addr = s_socket.accept()
print(f"Connected by {addr}")

data = conn.recv(1024)
print("Received:", data.decode())

conn.close()
s_socket.close()
