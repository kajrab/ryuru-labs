from scapy.all import *

ip = "YOUR IP"
port = 9999

# Building SYN packet
syn = IP(dst=ip) / TCP(dport=port, flags="S")

# Send and recieve the response
response = sr1(syn, timeout=2, verbose=0)

if response:
    if response[TCP].flags == "SA":
        print("SYN-ACK received!")

        # Step 2: Send ACK
        ack = IP(dst=ip) / TCP(
            sport=response[TCP].dport,
            dport=port,
            flags="A",
            seq=response[TCP].ack,
            ack=response[TCP].seq + 1,
        )

        send(ack, verbose=0)
        print("Handshake completed!")

    elif response[TCP].flags == "R":
        print(f"RST received! Port {port} is closed")
else:
    print("No response!")
