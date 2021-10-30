import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
result = response.json()

print('---------------------------')
print('Request response: ')
print(response)
print('---------------------------')
print('')

print('---------------------------')
print('Request json result: ')
print(result)
print('---------------------------')
print('')

print('---------------------------')
title = result['title']
print('Extracting Title value from dictionary: ' + title)
print('---------------------------')
print('')

