import requests
import base64

API_KEY = "d496c58773c720ecd20f7b71e54f052e819f6edc10a9eb4aae8bff4aac3d86e3"

url_prueba = "http://harmonycourtesy.cn/toyota60-v2w/tb.php?mo=fo1675893163934"

url_id = base64.urlsafe_b64encode(url_prueba.encode()).decode().strip("=")


url = "https://www.virustotal.com/api/v3/urls/" + url_id


headers = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
    "x-apikey": API_KEY
}

response = requests.get(url, headers=headers)

print(response.text)