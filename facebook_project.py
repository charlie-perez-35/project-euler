#%%
import pandas as pd

# locally stored csv file
filepath = r"C:\Users\charl\Downloads\MSDS-Orientation-Computer-Survey.csv"
table = pd.read_csv(filepath)

print(table)

#%%
import datetime
# for object in table:
   # if object["Timestamp"] <= 12/12/2024:
      #  table.drop(object)

print(type(table["Timestamp"][0]))
# %%

table["Timestamp"] = pd.to_datetime(table["Timestamp"], format = "%m/%d/%Y %H:%M")
print(table["Timestamp"][1])
# %%

data_classof2024 = table[table["Timestamp"].dt.year >= 2024]
print(data_classof2024)
print(data_classof2024["What is your github user name?"].unique())
print(data_classof2024["What is your github user name?"].value_counts())
# %%
# clearly some duplicates happening
# set up process to filter out duplicates


cleaned_2024 = data_classof2024.drop_duplicates(subset=["What is your github user name?"])

print(cleaned_2024)
# %%
import seaborn as sns
import matplotlib.pyplot as plt


# %%

data=cleaned_2024["CPU Cycle Rate (in GHz)"]
print(data.unique())

#%%

cleaned_2024 = cleaned_2024[cleaned_2024["CPU Cycle Rate (in GHz)"] <= 5]
data=cleaned_2024["CPU Cycle Rate (in GHz)"]
print(data.unique())

#%%

sns.histplot(data=data, bins=5, kde=False, color='skyblue')

plt.xlabel('Cycle Rate')
plt.ylabel('Frequency')
plt.title('Histogram of CPU Cycle Rate (in GHz), MSDS class of 2025')

plt.show()