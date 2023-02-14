import requests
from scapy.all import *
import time
import base64
import socket


packet_list = []

results = []


# Virus total
API_KEY = "d496c58773c720ecd20f7b71e54f052e819f6edc10a9eb4aae8bff4aac3d86e3"

headers = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
    "x-apikey": API_KEY
}


# Se ejecuta cuando se detecta un paquete
def react( packet_list ):
    # print(ip_list)
    print("...")

    def read_pkt(pkt):
        packet_list.append(pkt[IP])
      
        print("Source: " + pkt[IP].src + " Destination: " + pkt[IP].dst)

        # if IP in pkt:
        #     if pkt[IP].dst in ip_list:
        #       elif pkt[IP].src in ip_list:
        #         print("detected source ip: " + pkt[IP].src)
        # else:
        #     pass

    return read_pkt


def save_packets():
    with open("packets.txt", "w") as packet_file:
        for packet in packet_list:
            packet_file.write(str(packet) + '\n')


def save_results():
    with open("results.txt", "w") as results_file:
        for result in results:
            results_file.write(str(result) + '\n')


def resolve_url(ip_address):
    try:
        host_name = socket.gethostbyaddr(ip_address)
        return host_name[0]
    except socket.herror:
        print("No se pudo encontrar el nombre de host")

def get_url_id(url):
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    return url_id

def analyze_url(url):
    url_id = get_url_id(url)

    url_virus_total = "https://www.virustotal.com/api/v3/urls/" + url_id

    response = requests.get(url_virus_total, headers=headers)

    if response.status_code == 200:
      return response.json()["data"]["attributes"]["last_analysis_stats"]


def save_data_db(data):
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    for key, value in data.items():
        data = {
            "url": key,
            "malicious": value
        }
        db.child("urls").push(data)

def http_filter(packet):
    print(packet)
    return 'GET' in str(packet) or 'POST' in str(packet)


def capture_packets_and_analyze(time):

    global packet_list
    print("Capturando paquetes...")
    
    # Filtrar paquetes HTTP
    paquetes = sniff(iface="Wi-Fi", prn=http_filter, filter="tcp && not tcp port 22", timeout=time)
    wrpcap("paquetes.pcap", paquetes)
    print("Paquetes capturados")
    print(paquetes)

    save_packets()

    for pkt in packet_list:
         # mostrar las direcciones ip
        if "192.168" not in pkt[IP].dst:
          
            ip = pkt[IP].dst;

            url = resolve_url(ip)

            if url is not None:
              print("Analizando: " + url)

              res = analyze_url(url)
          
              print(res)
            
              print("--------------------------------------------")
         

    save_results()




capture_packets_and_analyze(10)

