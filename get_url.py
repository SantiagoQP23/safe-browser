


import ipinfo
access_token = 'a6f84bebfa76ba'

# import socket
# def get_url():
    
#     try:
#         host_name = socket.gethostbyaddr(ip_address)
#         print(host_name)
#     except socket.herror:
#         print("No se pudo encontrar el nombre de host")



def get_info_ip(ip_address):
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    return details

