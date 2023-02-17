from scapy.all import *

from datetime import datetime
import analyze_packets 

from tqdm import tqdm

from database import CaptureService, DestinationIPService, IPAnalysisService

packet_list = []

results = []

import get_url

def analyze_and_save_packets_db():
    
    captureService = CaptureService()
    destinationIpService = DestinationIPService()
    ipAnalysisService = IPAnalysisService()
    
    packets = rdpcap("paquetes.pcap")
    for pkt in tqdm(packets, desc="Analizando paquetes capturados", bar_format="{l_bar}{bar:10}{r_bar}{bar:-10b}"):
        
        ip_dst = pkt[IP].dst
        if "192.168" not in ip_dst:

          exist_info_ip = destinationIpService.find_one({"ip": ip_dst})

          if exist_info_ip is None:
             
              
              analysis = analyze_packets.analyze_ip(ip_dst)

              id_analysis = ipAnalysisService.insert(analysis)

              ip_info = get_url.get_info_ip(ip_dst)

              ip_info_with_analysis_id = dict(ip_info.all, ip_analysis_id=id_analysis)
              
              id_info_ip = destinationIpService.insert(ip_info_with_analysis_id)
          else: 
              id_info_ip = exist_info_ip["_id"]

          capture = {
              "ip_dst_info": id_info_ip,
              "ip_dst": pkt[IP].dst,
              "port_dst": str(pkt[TCP].dport),
              "ip_src": pkt[IP].src,
              "port_src": str(pkt[TCP].sport),
              "createdAt": datetime.now(),
              

          }

          captureService.insert(capture)



def http_filter(packet):
    print(packet)

def capture_packets(time):
    
    conf.promisc = True

    # paquetes = sniff(iface="Wi-Fi", prn=http_filter, filter="tcp port 80", timeout=time)
    paquetes = sniff(iface="Wi-Fi", prn=http_filter, filter="tcp && not tcp port 22", timeout=time, promisc=True)
    #paquetes = sniff(iface="Ethernet", prn=http_filter, filter="tcp && not tcp port 22", timeout=time)

    wrpcap("paquetes.pcap", paquetes)

    print("Resumen de paquetes capturados")
    print(paquetes)

