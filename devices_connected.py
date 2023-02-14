from scapy.layers.l2 import arp

arp_table = arp()
for entry in arp_table:
    print(entry)