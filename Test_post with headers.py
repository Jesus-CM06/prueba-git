import requests
import json
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers =  {"Content-Type":"application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
result = response.json()

print('---------------------------')
print('JSON.DUMPS: ')
print(todo)
print(json.dumps(todo))
print('---------------------------')
print('')

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