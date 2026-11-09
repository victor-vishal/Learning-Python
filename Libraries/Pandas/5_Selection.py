import pandas as pd

# df = pd.read_clipboard() # reads data from clipboard and creates a dataframe
# df.to_csv('clipboard.csv')

df = pd.read_csv('Libraries\Pandas\pokemons.csv')
# print(df)

# COLUMN SELECTION
# Syntax: df['column_name']
print(df['Name'].to_string())

print(df[['Name', 'Legendary']].to_string())
# to print only legendary pokemons we can use boolean indexing
df_legendary = df[df['Legendary'] == True].reset_index(drop=True) #ignore_index=True doesnt work outside methods like concat
print(df_legendary.to_string())