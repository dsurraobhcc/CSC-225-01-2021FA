import csv

'''
Using the Boston after hours construction data, create a new CSV file
with construction data only for Jamaica Plain, zip code 02130
'''

# open source file for reading
# with open('data/boston_after_hours_construction.csv', newline='') as f:
#     reader = csv.DictReader(f)

# open destination file for writing


# do some filtering here and write to destination file

# close source file
# close destination file

source = open('data/boston_after_hours_construction.csv','r')
destination = open('data/only_jp.csv','w', newline='')
reader = csv.reader(source) #returns reader object
writer = csv.writer(destination)
for row in reader:
    # print(row[3]) #prints addresses
    if '02130' in row[3]:
        print(row[3]) #prints addresses in 02130 zip code
        writer.writerow(row)
        
source.close()
destination.close()