import socket

SERVER_ADDR = ("127.0.0.1", 8732)
BUFFER_SIZE = 1024

s_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_socket.bind(SERVER_ADDR)

s_socket.settimeout(1.0)

print("Ready to receive")

try:
    while True:
        try:
            data, addr = s_socket.recvfrom(BUFFER_SIZE)
            print(f"Received from {addr}: {data.decode()}")
            s_socket.sendto(b"Message received", addr)

        except socket.timeout:
            continue

except KeyboardInterrupt:
    print("Server shutting down.")

except socket.error as e:
    print(f"Socket error: {e}")

finally:
    s_socket.close()
