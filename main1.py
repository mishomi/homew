import csv

with open ("titanic.csv ", 'r') as csvFile:
    reader = csv.reader(csvFile)
    with open ("survived.csv", 'w') as csvwrite:
        csvWriter = csv.writer(csvwrite, delimiter=',')
        next(reader)
        for i in reader:
            if i[1]=='1':
                csvWriter.writerow(i)
    with open("survived.csv", 'r') as csread:
        for i in csread:
            print(i)