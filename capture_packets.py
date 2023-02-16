from scapy.all import *


import analyze_packets 


packet_list = []

results = []

def save_packets():
    with open("packets.txt", "w") as packet_file:
        for packet in packet_list:
            packet_file.write(str(packet) + '\n')


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

