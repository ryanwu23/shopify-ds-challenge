import csv

total = 0 # keep track of total to verify AOV
count = -1 # keep track of how many orders to verify AOV
listOfOrderValues = [] # add all orders to find median
with open('shopifyChallenge.csv') as csvfile: # opening the csv file and reading each row
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if count != -1: # to skip over the first row which is all the column names
            listOfOrderValues.append(int(row[3])) # adding the order values which is 4th in the row
            total += int(row[3])
        count += 1

listOfOrderValues.sort() # sorting list then finding middle for the median value
if len(listOfOrderValues) % 2 == 1:
    median = listOfOrderValues[int(len(listOfOrderValues)/2)]
else:
    median = (listOfOrderValues[int(len(listOfOrderValues)/2)] + listOfOrderValues[int((len(listOfOrderValues)/2)-1)])/2
print("Average Order Value: " + str(total/count))
print("Median Order Value: " + str(median))