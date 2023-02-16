

import socket


import pprint

ip_address = "142.250.78.97"

import ipinfo

access_token = 'a6f84bebfa76ba'


def get_url():
    
    try:
        host_name = socket.gethostbyaddr(ip_address)
        print(host_name)
    except socket.herror:
        print("No se pudo encontrar el nombre de host")



def get_url_from_ip(ip_address):
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    return details

get_url_from_ip(ip_address)
