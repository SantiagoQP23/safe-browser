from scapy.all import *

from datetime import datetime
import analyze_packets 

from tqdm import tqdm

from database import CaptureService, DestinationIPService, IPAnalysisService

packet_list = []

results = []

import get_url





def save_packets_db():
    
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


def save_results():
    with open("results.txt", "w") as results_file:
        for result in results:
            results_file.write(str(result) + '\n')




# def save_data_db(data):
#     firebase = pyrebase.initialize_app(config)
#     db = firebase.database()

#     for key, value in data.items():
#         data = {
#             "url": key,
#             "malicious": value
#         }
#         db.child("urls").push(data)

def http_filter(packet):
    
    print(packet)
   
    # if "192.168" not in ip:
            

    #   url = resolve_url(ip)

    #   if url is None: 
    #       return
      
    #   print("Petición a: " + " ip: " + ip + "url: " +  url )

    #   url_id = get_url_id(url)

    #   if url is not None:

    #       res = analyze_packets.analyze_url(url_id)

    #       print(res)

    #print("Destino", )
    
    #return 'GET' in str(packet) or 'POST' in str(packet)


def capture_packets(time):

    print("--------------------------------------------")
    print("   Capturando paquetes           ")
    print("--------------------------------------------")

    # paquetes = sniff(iface="Wi-Fi", prn=http_filter, filter="tcp port 80", timeout=time)
    paquetes = sniff(iface="Wi-Fi", prn=http_filter, filter="tcp && not tcp port 22", timeout=time)

    wrpcap("paquetes.pcap", paquetes)

    print("Cantidad de paquetes capturados")
    print(paquetes)


    # for pkt in packet_list:
    #      # mostrar las direcciones ip
    #     if "192.168" not in pkt[IP].dst:
          
    #         ip = pkt[IP].dst;

    #         url = resolve_url(ip)

    #         if url is not None:
    #           print("Analizando: " + url)

    #           res = analyze_url(url)
          
    #           print(res)
            
    #           print("--------------------------------------------")
         

    # save_results()

#capture_packets(10)
# analyze_packets.analyze()

