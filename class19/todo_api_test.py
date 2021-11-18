"""
To do API: <your base url here>

The API used in class is posted in Moodle.

Or, build your own API using this tutorial: 
https://wsvincent.com/django-rest-framework-react-tutorial/
"""

import requests

base_url = <your api here>

# fetch data using an HTTP GET
# resp = requests.get(base_url)
# data = resp.json()
# [print(todo['title']) for todo in data]

# add a todo using an HTTP POST (verb/method)
my_next_todo = 'Complete class exercise today'
my_next_todo_desc = 'Class exercise on November 18th'

resp = requests.post(base_url, 
    data = {'title': my_next_todo, 'description': my_next_todo_desc})
data = resp.json()
todo_id = data['id']
print(f'newly created todo id: {todo_id}')



resp = requests.put(base_url + '13/', 
    data = {'title': my_next_todo, 'description': my_next_todo_desc})
print(resp.json())

resp = requests.patch(base_url + '13/', 
    data = {'title': my_next_todo})
print(resp.json())

# resp = requests.delete(base_url + '12/')
# print(resp)