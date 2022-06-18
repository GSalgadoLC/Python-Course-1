import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction id", "product id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 2])
    writer.writerow([1002, 3, 7])


with open("data.csv") as file:
    reader = csv.reader(file)
    print(list(reader))
    for row in reader:
        print(row)
