import csv

#1
datos=[]
y=["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2011","2012","2013","2014"]

with open("greenhouse_gas_inventory_data_data.csv") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
         if row[-1]  not in y:
              datos.append([float(row[-1])])

              datos.sort(reverse=True)
print(datos[:5])








"""datos=[]
with open("greenhouse_gas_inventory_data_data.csv") as csvFile:
     reader=csv.DictReader(csvFile)
     for row in reader:
          print(row["country_or_area"],row ["year"])

          



#2
pop=[]
val=["--","NA"]
contex=["World","Country","Asia & Oceania","Africa","Europe","Central & South America", "North America","Eurasia","Middle East"]
with open("populationbycountry19802010millions.csv") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
         if row[-1] not in val and row[0] not in contex:
              pop.append([float(row[-1]),row[0]])

              pop.sort(reverse=True)


print(pop[:5])"""






