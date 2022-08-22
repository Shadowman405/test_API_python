import requests

url = 'https://api.chucknorris.io/jokes/random'
result = requests.request('get',url)
assert 200 == result.status_code
if result.status_code == 200:
    print('Success')
else:
    print('Failed')

print(result.text)