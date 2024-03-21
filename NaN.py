import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)
df =  pd.DataFrame(data,["a","c","e","f","h"],["column_1","column_2","column_3"])

# We reindexed the data frame
df = df.reindex(["a","b","c","d","e","f","g","h"])

result = df.drop("column_1",axis = 1) # We deleted column 1

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10 ]
df["column_4"] = newColumn

result = df.isnull() # Returns TRUE for NaN values in the data frame
result = df.notnull() # Returns False for NaN values in the data frame

result = df.isnull().sum() # Shows how many NaN values there are in each column
result = df["column_1"].isnull().sum()
result = df[df["column_1"].isnull()]["column_1"]

result = df.dropna() # By default, axis=0, brings rows or columns that do not contain NaN

result = df.dropna(how = "any") # Deletes rows if any NaN is present in the row
result = df.dropna(how = "all") # Deletes rows where all values are NaN
result = df.dropna(subset = ["column_1","column_2"],how = "all")
result = df.dropna(thresh = 3) # Minimum number of non-NaN values required

result = df.fillna(value = 1) # Allows us to fill NaN values with desired values
result = df.fillna(value = "no input")

# We can find the average of the DataFrame and fill NaN values with this average
def mid (df):
    result = df.sum().sum()  # Total number of elements in the DataFrame
    resul = df.size  # Total number of elements in df (32 in total)
    resu = df.isnull().sum().sum()  # Total of 13 NaN values
    average = result / (resul - resu)
    newDf = df.fillna(value = average )
    return newDf

print(mid(df),"\n","\n",df)  

#data["Name"] = data["Name"].str.upper() # Converts the entire Name column to uppercase
#data["Name"] = data["Name"].str.lower() # Writes in lowercase
#data["Index"] = data["Name"].str.find("a") # Finds the index of the letter 'a' in the Name column and assigns it to a new column
#data = data.Name.str.contains("Jordan") # Searches for 'Jordan' in the Name column, returns True or False
#data = data[data.Name.str.contains("Jordan")] # Selects rows that contain 'Jordan'
#data = data.Team.str.replace(" ","_") # Replaces spaces in the Team column with underscores
# Select rows with only two parts

data = pd.read_csv("nba.csv")

data.dropna(inplace = True) # Deletes NaN values directly from the original file

data = data[data["Name"].str.strip().str.split().str.len() ==2]
new_order = ["FirstName", "LastName",'Team', 'Number', 'Position', 'Age', 'Height', 'Weight', 'College', 'Salary']
try:
    print("Single Name Entries")
    data[["FirstName", "LastName"]] = data["Name"].str.split(expand=True)
 
except ValueError:
    print("Double Name Entries")
    data[["FirstName", "MiddleName","LastName"]] = data["Name"].str.split(expand=True)
    data["FirstName"] = data["FirstName"] + " " + data["MiddleName"]
    data = data.drop(["MiddleName"],axis=1)
    print(data)
    print(data.columns)
finally:
    data = data.drop("Name", axis=1)
    data = data.iloc[:,[8,9,0,1,2,3,4,5,6,7]]

print(data)
