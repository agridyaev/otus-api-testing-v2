import requests

resp = requests.get(
    'https://httpbin.org//basic-auth/user/password',
    auth=('user', 'password')
)
print(f'{resp.status_code} - {resp.text}')

resp = requests.get('https://httpbin.org//basic-auth/user/password')
print(f'{resp.status_code} - {resp.text}')
