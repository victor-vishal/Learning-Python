import pandas as pd
df = pd.read_csv(r'Libraries\Pandas\pokemons.csv', index_col="Name")
# print(df.to_string())
# filtering is basically keeping the row that match the condition

fast_pokemon = df[df['Speed'] >= 100]
# Syntax: df[df['column_name'] condition value]

# print(fast_pokemon["Name"].to_string()) # Gives error because the index is set to 'Name' column and index is not a column anymore
# but since it is the index it prints by default along with any other columns we select
print(fast_pokemon[["Type 1", "Speed"]].to_string())

#for multiple conditions we use bitwise operator and put the conditional dataframe in parenthesis
# Syntax: df[  (df['col]condition)    bitwiseOPERATOR   (df['col2] condition2)]
water_pokemon = df[(df['Type 1'] == 'Water') | 
                   (df['Type 2'] == 'Water')] # using logical (or) instead of bitwise(|) raises error
print(water_pokemon.to_string())


fire_flying_pokemon = df[(df['Type 1'] == 'Fire') & 
                         (df['Type 2'] == 'Flying')]

print(fire_flying_pokemon)