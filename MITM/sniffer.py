from scapy.all import *

def process(packet):
    if packet.haslayer(Raw) and packet.haslayer(TCP):
        src = packet[IP].src
        dst = packet[IP].dst
        payload = packet[Raw].load
        print(f"[{src} -> {dst}] {payload}")

sniff(prn=process, store=False)
