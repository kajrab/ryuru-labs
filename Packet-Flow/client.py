import socket

c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c_socket.connect(("127.0.0.1", 6573))

message = "Data here!"

c_socket.send(message.encode())

c_socket.close()
