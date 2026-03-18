from scapy.all import *

ip = "8.8.8.8"

packet = IP(dst=ip) / ICMP()
response = sr1(packet, timeout=2, verbose=0)

if response:
    print("Active!")
else:
    print("No response")
