# Additional note: This reply script can be used for attack vectors, which is not the intended purpose here.
# It's only demonstrating how it works for educational purposes.
# Please do not use it on any system or network without proper permission.

import socket
from scapy.all import *

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 443))
        return s.getsockname()[0]
    finally:
        s.close()

def get_mac():
    try:
        return get_if_hwaddr(conf.iface)
    except Exception as e:
        raise RuntimeError(f"Couldn't get MAC address: {e}")

def arp_reply(target_ip, target_mac):
    try:
        ip = get_ip()
        mac = get_mac()

        pkt = Ether(dst=target_mac) / ARP(
            op=2, hwsrc=mac, psrc=ip, hwdst=target_mac, pdst=target_ip
        )

        sendp(pkt)
        print(f"Reply sent to {target_ip}")

    except Exception as e:
        print(f"Error: {e}")

# Requester's IP and MAC
arp_reply("192.168.1.50", "aa:bb:cc:dd:ee:ff")
