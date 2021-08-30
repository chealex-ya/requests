import requests
import json
from pprint import pprint

TOKEN = 'AQAAAAAWfuB9AADLW-5o7_9o7UlHnZ3wMj8e8EU'
API_BASE_URL = "https://cloud-api.yandex.net/"

headers = {
    'accept': 'application/json',
    'authorization': f'OAuth {TOKEN}'
}

params = {
    'path': f"PY43/photo.pdf",
    'overwrite': True
}

url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
r = requests.get(url=url, params=params, headers=headers)
res = r.json()
print(json.dumps(res, sort_keys=True, indent=4, ensure_ascii=False))

upload = requests.put(url=res['href'], data=open('photo.pdf', 'rb'), params=params, headers=headers)
print(upload.status_code)