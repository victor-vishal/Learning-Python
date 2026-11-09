import pandas as pd


# to read a file we use read_filetype() method of pandas
df = pd.read_csv('pokemons.csv')
print(df) # prints first and last 5 rows of dataframe along with number of dimensions (rows and columns)
# to print all of data we use .to_string() method
print(df.to_string())
