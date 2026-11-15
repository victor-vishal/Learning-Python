import pandas as pd

# Data Cleaning in Pandas is a process of fixing or removing incorrect, incomplete or irrelevant data
# The process involves several steps:
# 1. Removing or replacing missing values
# 2. Correcting inconsistent data
# 3. Standardizing data
# 4. Fixing data types
# 5. Removing duplicates

df = pd.read_csv(r'Libraries\Pandas\pokemons.csv')
print(df)
# df.set_index("#")



# 1. DROP COLUMNS
print("\n\n\nDropping columns # and Legendary")
# Syntax: df.drop(columns=[list of column names]))
df0 = df.drop(columns= ['#', 'Legendary'])
print(df0)



# 2. HANDLING MISSING DATA
# Method 1- DROPPING ROWS
print("\n\n\nDropping rows with missing values in Type 2 column") # in type 2 columns there are some missing values, we will delete those rows using dropna() function

# Syntax: df.dropna(subset=[list of column names])
df1 = df.dropna(subset=['Type 2'])
# df.dropna(subset=['Type 2'], inplace=True)
# since default value of inplace parameter is False it returns a new dataframe that we are assigning to df variable again, updating it, We can bypass it using inplace = True as it modifies the original dataframe and returns None
print(df1)
print(df1.count()) # now all columns are having same number of values

# HANDLING MISSING DATA
# Method 2- FILLING MISSING VALUES
# we use fillna() function and pass a dictionary with column name as keys and a value to which the missing values will be filled, We can pass multiple columns and values in the dictionary
print("\n\n\nFilling missing values in Type 2 column with None")
# Syntax: fillna({'col1: value1, 'col2': value2})
df2 = df.fillna({"Type 2":"None"})
print(df2)



# 3 FIXING INCONSISTENT DATA - REPLACING VALUES
# df.replace(to_replace=None, value=None, inplace=False, regex=False)
print("\n\n\nReplacing Type 1 values Fire with Pyro, Water with Hydro , Grass with Dendro etc")
# syntax: df['col'].replace({old_value1: new_value1, old_value2: new_value2}, inplace= True or False)
df['Type 1'] = df["Type 1"].replace({"Fire" : "Pyro",
                                     "Water": "Hydro",
                                     "Grass": "Dendro",
                                     "Electric": "Electro",
                                     "Rock": "Geo"})
# when we select a column like df['Type 1'] it actually work like a series, now we are using this series object with replace() function, this replace function will return a new series which we are assigning back to the same series or column, updating the original column, we can bypass this using inplace = True parameter
print(df.to_string())



# 4. Standardizing Data - Changing the case of string values
print("\n\n\nStandardizing data - Changing the case of string values")
df['Name'] = df["Name"].str.lower()
print(df.to_string())

# 5. Fix Data Types
print("\n\n\nFixing data types")
print(df["Legendary"].dtype) # bool
df["Legendary"] = df["Legendary"].astype(int) # we can also pass data type in string format ("int")
print(df)
print(df["Legendary"].dtype) #int64



# 6. REMOVING DUPLICATES
# first create duplicates
df3 = df[df["Name"] == "bulbasaur"]
df3 = pd.concat([df] + [df3]*4, ignore_index=True) # ignore_index = True will reset the index of the new dataframe
print("\n\n\nDataset with duplicates 'bulbasaur'")
print(df3[df3["Name"] == "bulbasaur"])

# now removing duplicates
print("\n\n\nRemoving duplicates")
# Syntax: df.drop_duplicates(inplace=True) or df.drop_duplicates() and assign it to a new variable
# other arguments are:
# keep = 'first' (default) will keep the first occurrence of the duplicate and remove the rest
# keep = 'last' will keep the last occurrence of the duplicate and remove the rest
# keep = False will remove all occurrences of the duplicate

df3 = df3.drop_duplicates()
print(df3[df3["Name"] == "bulbasaur"])