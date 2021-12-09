# imports
import csv, pandas as pd, pprint

# 1. Using CSV
# read weather_data.csv and add data to weather_data list
with open("./files/weather_data.csv", mode="r") as data:
  # Read .csv file using csv library
  reader = csv.reader(data)
  # Declaring new list to include csv file data
  temperatues = list()  
  # Skip first row
  next(reader)
  # Iterate over each row and append temp data and casting it to int.
  for row in reader:
    temperatues.append(int(row[1]))

  print(temperatues, end="\n\n")


# Panadas
# Read csv file using pandas
data = pd.read_csv("./files/weather_data.csv")

# Every table in pandas is considered a DataFrame.
# Every column in pandas is considered a series.
print(type(data))

# Convert data to dict
data_dict = data.to_dict()
pprint.pprint(data_dict)

# Initialize a temp variable with temp column as the initial value
temp = data["temp"]
print("\n")
# Convert temp column in data "table" into a list
temp_list = temp.to_list()
print(f"Temperature list: {temp_list}")

# Challenge: Calculate average temperature
avg_temp = sum(temp_list) / len(temp_list)
print(f"Average temperature is: {format(avg_temp, '.0f')}")

# OR
avg_temp2 = temp.mean()
print(format(avg_temp2, "0.0f"))

# Challenge: Calculate the MAX temp using data series method
max_temp = temp.max()
print(max_temp)

# We can also select columns in pandas table using dot .
condition = data.condition
print(condition, end="\n\n")

# Fetching entire row in a table 
# Fetch Monday row
monday = data[data.day == "Monday"]
print(monday, end="\n\n")
# Fetch monday condition
print(data[data.day == "Monday"].condition, end="\n\n")

# Challenge: return the row of data with the highest temp of the week
highest_temp_day = data[data.temp == temp.max()]
print(f"Highest temperature day data:\n{highest_temp_day}", end="\n\n")

monday_temp = data[data.day == "Monday"].temp
f = (monday_temp * 2) + 30
print(f, end="\n\n")


# Creating DataFrame from scratch

stds_scrs = {
  "students": ["Amy", "James", "Angela"],
  "scores": [76, 56, 65]
}

stds_scrs_df = pd.DataFrame(stds_scrs)
print(stds_scrs_df)

# convert dataframe to csv
stds_csv = stds_scrs_df.to_csv("./files/students.csv")


