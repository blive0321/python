#csv = comma seperated values
import csv
fruit = [
    ['rice','soup'],
    ['noodles','milk'],
    ['eggs','onion'],
    ]

#write
print("write to csv...")
with open('fruit','wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(fruit)

#read
with open('fruit','rt') as fin:
    cin = csv.reader(fin)
    fruit = [row for row in cin]

print("read from csv...")
print(fruit)
