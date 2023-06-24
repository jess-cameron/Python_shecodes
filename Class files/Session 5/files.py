import csv

# with open("dogs_are_awesome.csv") as my_file:
#     csv_reader = csv.reader(my_file)
#     for row in csv_reader:
#         print(row)

# with open("dogs_are_awesome.csv") as my_file:
#     csv_writer = csv.writer(my_file)
#     csv_writer.writerow("Hello")

population = []
with open(file="2016_pilbara.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        population.append(line)

# print(population)

# for age_group in population:
#     print(f"{age_group[0]} {age_group[1]}")

with open(file="population.csv", mode="w") as csv_file:
    csv_writer = csv.writer(csv_file)

    for age_group in population:
        csv_writer.writerow({age_group[0], age_group[1]})
        