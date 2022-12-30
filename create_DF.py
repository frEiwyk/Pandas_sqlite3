import pandas as pd

column = ["Mariya", "Batman", "Spongebob"]
titled_columns = {"name": column,
                "height": [1.67, 1.9, 0.25],
                "weight": [54, 100, 1]}        # using a dictionary to create several titled columns
data = pd.DataFrame(titled_columns)            # better view of our dictionary (as dataframe)


# below are different approaches to selecting specific values/parts of the dataset created with pd.DataFrame
selected_column = data["weight"][1]
selected_row = data.iloc[1]["weight"]

# manipulating dataframe values (calculating with them, appending them)
bmi = []
# weight/(height**2)
for i in range(len(data)):
    bmi_score = data["weight"][i]/(data["height"][i]**2)
    bmi.append(bmi_score)

data["bmi"] = bmi

# save dataframe to a file (by default, comma delimited)
# "\t" is tab delimiter (.csv can be replaced with e.g. .txt)
# index=False deletes the first column (indexes created by pd.DataFrame)
data.to_csv("bmi.csv", index=False, sep="\t")

print(data)

