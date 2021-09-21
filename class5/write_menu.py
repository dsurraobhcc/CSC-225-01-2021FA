import csv

menu = [
    {'item': 'Pancakes', 'price': 4},
    {'item': 'Egg sandwich', 'price': 3},
    {'item': 'Coffee', 'price': 1.50}
]

with open('menu.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['item', 'price'])
    writer.writeheader()
    for item in menu:
        writer.writerow(item)