
from prettytable import PrettyTable

from tqdm import tqdm

from database import CaptureService, DestinationIPService, IPAnalysisService

def show_report_captures():
    
   
    captureService = CaptureService()

    table = PrettyTable()

    table.field_names = [ "N° ",  "IP Origen", "Puerto Origen", "IP Destino", "Puerto Destino"]

    captures = captureService.find({})

    count = captureService.count({});

    print("Total de capturas: ", count)

    #Contador 
    i = 0

    for capture in captures:
        table.add_row([i, capture["ip_src"], capture["port_src"], capture["ip_dst"], capture["port_dst"]])
        i = i + 1

    print(table)


def show_reports_ip():
    
   
    destinationIpService = DestinationIPService()

    table = PrettyTable()

    table.field_names = [ "IP", "hostname", "País", "Ciudad", "Latitud", "Longitud",  "Organización"]

    ips = destinationIpService.find({})

    count = destinationIpService.count({});

    print("Total de IPs: ", count)


    for ip in ips:
        if "hostname" in ip:
          hostname = ip["hostname"]
        else:
          hostname = "No disponible"
        table.add_row([ ip["ip"], hostname , ip["country"], ip["city"], ip["latitude"], ip["longitude"], ip["org"]])

    print(table)

def show_reports_analysis():
   
    destinationIpService = DestinationIPService()
    ipAnalysisService = IPAnalysisService()

    table = PrettyTable()

    #table.field_names = [ "IP", "Harmless", "Malicious", "Suspicious", "Undetected", "Timeout" ]

    # Encabezado en español
    table.field_names = [ "IP", "hostname", "Inofensivo", "Malicioso", "Sospechoso", "No detectado", "Tiempo de espera"]

    ips = destinationIpService.find({})

    count = destinationIpService.count({});

    print("Total ips analizadas: ", count);

    for ip in tqdm(ips, desc="Generando reporte", ):
        a = ipAnalysisService.find_one({"_id": ip["ip_analysis_id"]})
        if "hostname" in ip:
          hostname = ip["hostname"]
        else:
          hostname = "No disponible"

        table.add_row([ ip["ip"], hostname , a["harmless"], a["malicious"], a["suspicious"] , a["undetected"], a["timeout"]])

    print(table)
   
