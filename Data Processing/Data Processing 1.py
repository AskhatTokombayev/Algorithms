import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'sitka_weather_07-2014.csv.txt'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#for index, column_header in enumerate(header_row):
#    print(index, column_header)

    highs = []
    lows = []
    date =[]
    for row in reader:
        high = int(row[1])
        low = int(row[2])
        lows.append(low)
        highs.append(high)
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        #print(current_date)
        date.append(current_date)
    print(highs)
    print(date)


plt.plot(date,highs, c='red', alpha =0.5)
plt.plot(date,lows, c='blue', alpha =0.5)
plt.fill_between(date,highs,lows, facecolor='blue',alpha=0.1)

plt.xlabel('', fontsize=14)
plt.ylabel('Temperature, F', fontsize=14)
plt.show()