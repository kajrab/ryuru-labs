import socket

SERVER_ADDR = ("127.0.0.1", 8732)
TIMEOUT = 5

c_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c_socket.bind(("127.0.0.1", 0))
c_socket.settimeout(TIMEOUT)

try:
    c_socket.sendto(b"This is client!", SERVER_ADDR)
    
    data, addr = c_socket.recvfrom(1024)
    print(f"Server: {data.decode()}")

except socket.timeout:
    print("No response - packet may have been lost.")
except socket.error as e:
    print(f"Socket error: {e}")
finally:
    c_socket.close()
