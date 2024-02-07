import csv

with open("organizations-100.csv", 'r') as csvFile:
    reader = csv.reader(csvFile)
    with open("sorted.csv", 'w') as csvwrite:
        csvWriter = csv.writer(csvwrite, delimiter=',')
        next(reader)
        sortedData = sorted(reader, key=lambda x: int(x[8]))
        csvWriter.writerows(sortedData)
with open("sorted.csv", 'r') as csread:
    for row in csread:
        print(row)
