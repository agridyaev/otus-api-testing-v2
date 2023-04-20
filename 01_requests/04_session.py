import requests

sess = requests.Session()
sess.auth = ('user', 'password')

resp = sess.get('https://httpbin.org/basic-auth/user/password')
print(resp.text)

resp2 = sess.get('https://httpbin.org/basic-auth/user/password')
print(resp2.text)
