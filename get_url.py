


import ipinfo
access_token = 'a6f84bebfa76ba'

def get_info_ip(ip_address):
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    return details

