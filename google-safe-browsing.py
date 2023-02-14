
import requests

API_KEY = "AIzaSyCyRs2xQgOX04HhsehouRuquWVuqFtIE6k"

CLIENT_ID = "172288460765-frvsquatjembousnmfueqlcsv99fcdpr.apps.googleusercontent.com"

{
  "data": {
    "type": "analysis",
    "id": "u-114fb86b9b4e868f8bac2249eb5c444b545f0240c3dadd23312a0bc1622b5488-1676056423"
  }
}

url = "https://www.twitter.com"


response = requests.get(f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}",
          headers={"Content-Type": "application/json"},
          json={"client": {"clientId": CLIENT_ID, "clientVersion": "1.0"},
                "threatInfo": {"threatTypes": ["THREAT_TYPE_UNSPECIFIED"],
                                "platformTypes": ["ANY_PLATFORM"],
                                "threatEntryTypes": ["URL"],
                                "threatEntries": [{"url": url}]}})

print(response)

# Verifique la respuesta de la API para determinar si la URL es segura o no
if response.status_code == 200:
    if response.json() == {}:
        print(f"La URL {url} es segura.")
    else:
        print(f"La URL {url} es insegura.")
else:
    print("Error en la solicitud.")
