from scapy.all import *
import requests
import base64

# Virus total
API_KEY = "d496c58773c720ecd20f7b71e54f052e819f6edc10a9eb4aae8bff4aac3d86e3"

headers = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
    "x-apikey": API_KEY
}

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

