import csv

with open("organizations-100.csv", 'r') as csvFile:
    reader = csv.reader(csvFile)
    with open("ssl_companies.csv", 'w') as csvwrite:
        csvWriter = csv.writer(csvwrite, delimiter=',')

        next(reader)
        for row in reader:
            if "https" in row[3] :
                csvWriter.writerow([row[0], row[1], row[2], row[3], row[7], row[8]])

with open("ssl_companies.csv", 'r') as csread:
    for row in csread:
        print(row)
