from scapy.all import *

target = "first_target_ip"
inner_dst = "real_target_ip"

inner_packet = IP(dst=inner_dst) / TCP(dport=80, flags="S")
gre_packet = IP(dst=target) / GRE() / inner_packet

send(gre_packet, verbose=0)
print("GRE packet sent")
