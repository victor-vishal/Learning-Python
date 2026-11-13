import pandas as pd

# Aggregate functions are used to reduce the data into a single value or a summary statistic.
# often used with groupby() function

df = pd.read_csv(r'Libraries\Pandas\pokemons.csv')
print(df.columns)
# print(df.mean())# gives type error as mean can only be found of columns with numerical values
print(df.mean(numeric_only=True))# numeric_only = True will only consider the numerical columns for mean calculations
# other aggregate functions include sum(), min(), max(), median(), std() etc. work similarly to mean() and can be used with numeric_only = True parameter
# Syntax: df.aggregate_function(numeric_only=True)
print(df.max(numeric_only=True))
# while count() function doesnt need the parameter as it counts all the non-null values in the columns
print(df.count()) # Type 2 columns have 77 values only because not every pokemon has a second type

# FOR SINGLE COLUMNS
# Syntax: df['col'].aggregate_func() 
# since we only pass a single column we dont need to use numeric_only parameter
print('AvgHP: ', df['HP'].mean())
print('MaxHP: ', df['HP'].max())
print('STD of HP: ', df['HP'].std())
print('number of elements in HP column: ',df['HP'].count())