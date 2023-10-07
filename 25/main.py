import csv

with open('weather_data.csv') as file:
    read_data = csv.reader(file)
    data = []
    for row in read_data:
        data.append(row)
    # print(data)

import pandas

data = pandas.read_csv('weather_data.csv')
print(data)

print("Average temperature: " + str(round(sum(data['temp'].to_list()) / len(data['temp'].to_list()), 2)) + "°C.")
print("Max temperature: " + str(data["temp"].max()) + "°C.")

# get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# create dataframe from scratch
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
data = pandas.DataFrame(data_dict)
print(data)
