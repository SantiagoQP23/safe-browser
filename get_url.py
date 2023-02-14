

import socket

ip_address = "157.240.6.35"

try:
    host_name = socket.gethostbyaddr(ip_address)
    print(host_name[0])
except socket.herror:
    print("No se pudo encontrar el nombre de host")