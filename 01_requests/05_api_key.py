import requests

from test_data import DOG_FILE_PATH

sess = requests.Session()
sess.headers = {'api_key': 'special-key'}

json = {
    "name": "doggie",
    "photoUrls": [
        "https://cdn2.thedogapi.com/images/njDSq3gRF.jpg"
    ]
}

r = sess.post(
    url='https://petstore.swagger.io/v2/pet',
    json=json
)
print(r.json())

dog_id = r.json()['id']

with open(DOG_FILE_PATH, 'rb') as f:
    files = {'file': f,
             'type': 'image/jpeg'}

    r_upload = sess.post(
        url=f'https://petstore.swagger.io/v2/pet/{dog_id}/uploadImage',
        files=files
    )
    print(r_upload.json())
