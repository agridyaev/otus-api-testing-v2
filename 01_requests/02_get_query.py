import requests

query = {'lang': 'rus', 'id': 18}

r = requests.get('https://meowfacts.herokuapp.com/', params=query)

print(r.json())
print(r.url)
print()
