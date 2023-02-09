from scapy.all import *

packet_list = []

def main():
    
    ip_file = open("ip.txt", "r")  
    ip_list = ip_file.read().splitlines()

    global packet_list

   
    while True:
        
        sniff(iface="Wi-Fi", prn=react(ip_list, packet_list), filter="tcp && not tcp port 22", count=1)
        #input_value = input("Presiona una tecla para continuar o 'q' para salir: ")
        save_data()
    
   


def react(ip_list, packet_list):
    print(ip_list)
    print("Reaccionando...")
    def read_pkt(pkt):
        packet_list.append(pkt) 
        if IP in pkt:
            if pkt[IP].dst in ip_list:
                print("detected destiny ip: " + pkt[IP].dst)
            elif pkt[IP].src in ip_list:
                print("detected source ip: " + pkt[IP].src)
        else:
            pass

    return read_pkt


def save_data():
     with open("packets.txt", "w") as packet_file:
        for packet in packet_list:
            packet_file.write(str(packet) + '\n')


main()