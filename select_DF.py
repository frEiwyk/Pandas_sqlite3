import pandas as pd
import sqlite3

# since the data is saved with a non-standard delimiter, it has to be specified
# index column is assigned automatically
data = pd.read_csv("bmi.csv", sep="\t")
#print(data)

# connect to a database
connection = sqlite3.connect("gta.db")

# read data from a table called "gta" fomr inside the database
gta_data = pd.read_sql("SELECT * FROM gta", connection)

# print only the beginning (first 5 rows by default)
#print(gta_data.head(2))
# print only the end
#print(gta_data.tail(1))

# first "gta_data" is a filtering command, the second instance is the looked for column
filtered_row = gta_data[gta_data["city"] == "Liberty City"]

# if we want to replace particular values, we use .replace
replaced_city = gta_data.replace("Liberty City", "New York")
#print(filtered_row)
#print(replaced_city)

# remove data (axis=1 is columns, axis=0 is rows)
remove_column = gta_data.drop(["city", "release_year"], axis=1)
#print(remove_column)
remove_row = gta_data.iloc[1:4]
#print(remove_row)

# add new rows
new_row = {"release_year": "2021",
        "release_name": "New Title",
        "city": "Los Angeles"}

new_raw_data = gta_data.append(new_row, ignore_index=True)
print(new_raw_data)

# drop duplicates
data.drop_duplicates( subset=["ID"])        # if we accidentaly have duplicate entries (subset specifies the key to look for)

connection.close()