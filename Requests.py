import requests
from pprint import pprint

TOKEN = 'AQAAAAAWfuB9AADLW-5o7_9o7UlHnZ3wMj8e8EU'

API_BASE_URL = "https://cloud-api.yandex.net/"

headers = {
    'accept': 'application/json',
    'authorization': f'OAuth {TOKEN}'
}

# file_list_response = requests.get(API_BASE_URL + "v1/disk/resources/files", headers=headers)
#
# files = file_list_response.json()['items']
# photo = files[1]
# photo_response = requests.get(photo['file'])

# with open('photo.pdf', 'wb') as f:
#     f.write(photo_response.content)
#
# r = requests.get(API_BASE_URL + "v1/disk/resources/upload", params={'path': 'PY43/photo.pdf'}, headers=headers)
#
# upload_url = r.json()["href"]

img_url = "https://rusinfo.info/wp-content/uploads/1/7/0/1704eef07fafe960baddb607ce23b571.jpg"

# r = requests.put(upload_url, headers=headers, files={'f': open("photo.pdf", 'rb')})

upload = requests.post(API_BASE_URL + "v1/disk/resources/upload", headers=headers, params={'path': 'py43/img.jpeg', 'url': img_url})