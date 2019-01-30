import csv, time
def csvReader():
	rowCount=0
	with open('businessfile.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			print(row)
			rowCount+=1
	print('There are %d rows in the CSV file.'%rowCount)
initialTime = time.time()
cr=csvReader()
finalTime= time.time()


print('The CSV Reader took %s seconds to read the file.' %(finalTime - initialTime))
