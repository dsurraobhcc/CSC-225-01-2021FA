"""
To do API: <your base url here>

The API used in class is posted in Moodle.

Or, build your own API using this tutorial: 
https://wsvincent.com/django-rest-framework-react-tutorial/
"""

import requests

base_url = <your base url here>

# fetch data using an HTTP GET
resp = requests.get(base_url)
data = resp.json()
[print(todo['title']) for todo in data]

# add a todo using an HTTP POST
my_next_todo = 'Drink kombucha'
my_next_todo_desc = 'Drink kombucha after class'

resp = requests.post(base_url, 
    data = {'title': my_next_todo, 'description': my_next_todo_desc})
print(resp.text)

