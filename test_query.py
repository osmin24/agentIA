import urllib.request, urllib.error, json

req = urllib.request.Request(
    'http://127.0.0.1:8000/api/query', 
    data=json.dumps({"query": "hola"}).encode('utf-8'), 
    headers={'Content-Type': 'application/json'}
)
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print("Error:", e.read().decode())
