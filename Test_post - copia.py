import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
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

print('Holis')
print('Holis 2')