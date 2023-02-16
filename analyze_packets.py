from scapy.all import *
import requests
import base64


import pprint



import get_url

from database import CaptureService

# Virus total
API_KEY = "d496c58773c720ecd20f7b71e54f052e819f6edc10a9eb4aae8bff4aac3d86e3"


headers = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
    "x-apikey": API_KEY
}



url = "https://www.virustotal.com/api/v3/ip_addresses/54.233.186.89"

headers = {
    "accept": "application/json",
    "x-apikey": "d496c58773c720ecd20f7b71e54f052e819f6edc10a9eb4aae8bff4aac3d86e3"
}

response = requests.get(url, headers=headers)

print(response.text)

def analyze_ip(ip_address):
    url_virus_total = "https://www.virustotal.com/api/v3/ip_addresses/" + ip_address

    response = requests.get(url_virus_total, headers=headers)

    if response.status_code == 200:
      return response.json()["data"]["attributes"]["last_analysis_stats"]
    




def resolve_url(ip_address):
    try:
        host_name = socket.gethostbyaddr(ip_address)
        return host_name[0]
    except socket.herror:
        return

def get_url_id(url):
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    return url_id




def analyze_url(url):
    

    url_virus_total = "https://www.virustotal.com/api/v3/urls/" + url

    response = requests.get(url_virus_total, headers=headers)


    print(response.json())

    if response.status_code == 200:
      return response.json()["data"]["attributes"]["last_analysis_stats"]

def analyze():
    

    print("--------------------------------------------")
    print("   Analizando paquetes capturados           ")
    print("--------------------------------------------")
      
    packet_list = rdpcap("paquetes.pcap")

    for pkt in packet_list:
        # mostrar las direcciones ip
        ip_dst = pkt[IP].dst;

        if "192.168" not in ip_dst:
  
            print(pkt)

            info_ip = get_url.get_info_ip(ip_dst)

            pprint.pprint(info_ip.all)



            if hasattr(info_ip, 'hostname'):

              url = info_ip.hostname
              print("Analizando: " + url)
              url_id = get_url_id(url)

              res = analyze_url(url)
        
              print(res)

              #urlService.save_url(url, res)

              print("--------------------------------------------")

            # if url is not None:
            #   print("Analizando: " + url)

            #   res = analyze_url(url)
          
            #   print(res)
                
            #   print("--------------------------------------------")


#analyze()