import pandas as pd

# df = pd.read_clipboard() # reads data from clipboard and creates a dataframe
# df.to_csv('clipboard.csv')

df = pd.read_csv('Libraries\Pandas\pokemons.csv')
# print(df)

# COLUMN SELECTION
# Syntax: df['column_name']
print(df['Name'].to_string())
# to select multiple columns we pass a list of column names (double [[]])
print(df[['Name', 'Legendary']].to_string())
# to print only legendary pokemons we can use boolean indexing
df_legendary = df[df['Legendary'] == True].reset_index(drop=True) #ignore_index=True doesnt work outside methods like concat
print(df_legendary.to_string())

# ROW SELECTION
# Syntax: df.loc[row_index]
# print(df.loc[0].to_string()) # prints the first row
# for easier selection we can change the index to  'Name' column
# we can either set it while reading the file using
# df = pd.read_csv('Libraries\Pandas\pokemons.csv', index_col='Name')
# or by using the set_index method
print("\n\n\nIndex Changed to name")
df2= df.set_index('Name', inplace = False)
print(df2)

# Synatx:
# df.set_index(keys/column_name, drop=True, append=False, inplace=False)
# drop: to remove the column after setting it as index, True by default
# append: add the column to existing index creating multi-index, False by default
# inplace: modifies the original dataframe, false by default, if True it returns None else returns a new dataframe with index changed, that can be assigned to a new variable

print("Finding Charizard")
print(df2.loc['Charizard'].to_string()) #to_string() strips 'Name: Charizard, dtype: object' from the output, making it more readable
# print(df2.loc['Charizard'])

# to select only a few columns we use chain indexing
print('Selecting only few columns from a row')
#Syntax: df.loc[row, [col1, col2]]
print(df2.loc["Charizard", ["HP", "Attack"]])

print("\n\n\nSelecting multiple rows")
print(df2.loc['Charizard': 'Blastoise', ["HP", "Attack"]])

# using integer indexing
print("\n\nUsing integer indexing")
print(df2.iloc[20:25])

print("\nPrinting first three columns")
print(df2.iloc[20:25, 0:3]) #Syntax: df.iloc[rowStart:end, colStart:end] (end is exclusive)

# Finding a pokemon name:
pokemon = input("Enter name of Pokemon to find: ")

try:
    print(df2.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")