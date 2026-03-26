from scapy.all import *
import socket

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

def arp_request(target_ip):
    try:
        ip  = get_ip()
        mac = get_mac()

        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(
            op=1,
            hwsrc=mac,
            psrc=ip,
            hwdst="00:00:00:00:00:00",
            pdst=target_ip
        )

        r, _ = srp(pkt , timeout = 2)

        for sent, recv in r:
            print(f"IP: {recv.psrc}, MAC: {recv.hwsrc}")

    except Exception as e:
        print(f"Error: {e}")

# Must be changed to ur target computer's local IP
arp_request("192.168.1.50")
