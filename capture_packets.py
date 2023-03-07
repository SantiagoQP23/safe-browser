from scapy.all import *

from datetime import datetime
import analyze_packets 

from tqdm import tqdm

from database import CaptureService, DestinationIPService, IPAnalysisService, ConfigService

packet_list = []

results = []

import get_url


def set_interface(interface):
    configService = ConfigService()
    config = configService.find_one({})
    if config is None:
        configService.insert({"interface": interface})
        print("Interfaz asignada")
    else:
        configService.update({"interface": config["interface"]}, {"$set": {"interface": interface}})
        print("Interfaz actualizada")
    

def get_interface():
    configService = ConfigService()
    config = configService.find_one({})
    interface = "No asignada"
    if config is not None:
        interface = config["interface"]

    return interface



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
    
    interface = get_interface()

    if interface == "No asignada":
        print("No se ha asignado una interfaz, por favor asigne una interfaz")
        return

    # paquetes = sniff(iface="Wi-Fi", prn=http_filter, filter="tcp port 80", timeout=time)
    try:
        paquetes = sniff(iface=interface, prn=http_filter, filter="tcp && not tcp port 22", timeout=time, promisc=True)
    except:
        print("No se pudo capturar paquetes, verifique la interfaz asignada")
        paquetes = []
    #paquetes = sniff(iface="Ethernet", prn=http_filter, filter="tcp && not tcp port 22", timeout=time)

    wrpcap("paquetes.pcap", paquetes)

    print("Resumen de paquetes capturados")
    print(paquetes)

