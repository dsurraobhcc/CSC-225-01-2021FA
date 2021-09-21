import csv
from datetime import datetime

# with open('data/boston_after_hours_construction.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         # print only address in zip code 02130
#         if '02130' in row[3]:
#             print(row[3])

with open('data/boston_after_hours_construction.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # filter: get all construction starting in the future
        dt = datetime.strptime(row['startdate'], "%Y-%m-%d %H:%M:%S")
        if dt > datetime.now():
            print(row['startdate'], row['address'])