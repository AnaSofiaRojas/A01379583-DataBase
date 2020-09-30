import csv

gas=[]
data_e=["value","country_or_area"]
year="2010"
with open("greenhouse_gas_inventory_data_data.csv") as csvFile:
    reader1 =csv.reader(csvFile)
    for row in reader1:
            if row[2] not in data_e and row[1] in year: 
                gas.append([float(row[-2]), row[0]])
    gas.sort(reverse=True)

print(gas[:5])




pop=[]
v=["--","NA"]
co_e=["World","Country","Asia & Oceania","Africa","Europe","Central & South America", "North America","Eurasia","Middle East"]


with open("populationbycountry19802010millions.csv") as csvFile:
    reader =csv.reader(csvFile)
    for row in reader:
        if row[-1] not in v and row[0] not in co_e:
            pop.append([float(row[-1]), row[0]])
    
    pop.sort(reverse=True)

    print(pop[:5])






