import pandas as pd
# Dataframe is a 2Dimensional tabular data structure with rows and columns. it is like a spreadheet

pokemon = {
    'Name': ['Pikachu', 'Bulbasaur', 'Squirtle', 'Pidgeotto'],
    'Type': ['Thunder', 'Grass', 'Water', 'Flying']
}

df = pd.DataFrame(pokemon, index=[1,2,3,4]) #DataFrame is a constructor, while df is an object (df is short for dataframe)
print(df)

# when we pass a dictionary to DataFrame, the keys become the colyumn names and the value become rows
# we can also pass list, tuples etc

#index column name can also be changed by default it is null
# df.index.name = 'Pokedex Number'
# print(df)

# to access a single row we use loc[] or iloc[] methods
print(df.loc[1]) #loc is used to access rows by index label,
print()
print(df.iloc[0]) #iloc is used to access by index position (starts from 0)

## Adding a new column to dataframe
# Syntax: df['new_columnName'] = [value1, value2,...]
df['Evolution Stage'] = ['Stage 2', 'Stage 1', 'Stage 1', 'Stage 2']
print("Dataframe after adding a new column 'Evolution Stage': \n", df)
print()
# to access a single, multiple columns: Syntax: df['column1', 'column2']
print(df['Evolution Stage'])
# to access a single value from a column Syntax: df['column_name'][index of row]  (loc index not iloc or postion index)
print("Evolution Stage of Pikachu: ", df["Evolution Stage"][1]) # This method is called chain indexing

# To add a new row to the dataframe we can create a new dataframe then concatenate it with the existing dataframe
# Method 1: create a new dataframe column wise doesnt uses [] brackets
# syntax: pd.DataFrame({'col1: [values1], 'col2': [values2]})
new_pokemons = pd.DataFrame({
    'Name': ['Charmander', 'Jigglypuff'],
    'Type': ['Fire', 'Fairy'],
    'Evolution Stage': ['Stage 1', 'Stage 2']
})

#Concatenate: Syntax: pd.concat([df1, df2], ignore_index=True) #df1 would be placed first then df2
df = pd.concat([df, new_pokemons], ignore_index=True) # if not True the new rows will start from 0)
#ignore_index=True will reset the index of older dataframes and uses the default 0 to n indexing
print("\nDataframe after adding new rows: \n", df)

# Method 2: create a new dataframe row wise uses [] brackets
# syntax: pd.DataFrame([{row1}, {row2}])
new_pokemons = pd.DataFrame([
    {"Name": "Raichu", "Type": "Thunder", "Evolution Stage": "Stage 3"}, #row 1
    {"Name": "Charizard", "Type": "Fire", "Evolution Stage": "Stage 3"} #row2
])

df = pd.concat([new_pokemons, df], ignore_index=True)
#it can be seen that the first dataframe sent to concat is added first
print("\n\n",df)