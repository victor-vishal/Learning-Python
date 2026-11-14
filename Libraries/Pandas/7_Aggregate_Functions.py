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

# For multiple columns: We pass a list of column names
print(df[['HP', 'Attack']].mean())

# groupby() function is used to group the data based on a column and then apply aggregate functions on the grouped data
# Syntax: df.groupby('col').aggregate_func() or pass a list of columns to group by multiple columns

# group = df.groupby(['Type 1', 'Type 2']) # groupby() function returns a DataFrameGroupBy object (or a SeriesGroupBy if you select a single column)
group = df.groupby('Type 1') 
print(group['HP'].mean()) # it gives average HP of each Type 1 pokemon, 
# so basically the dataset is split into as many groups as there are unique values in type 1 column then it groups the similar value together
# in above code we apply mean() function on the data grouped by type 1, meaning it will give average HP of every Type 1 group

# to know average attack of each type 1
print(group['Attack'].mean().round(2)) #round(2) is a pandas function to round the values upto the passed integer value

# total HP of each group
print(group['HP'].sum())

# Weakest pokemon attack in each Type 1 (minimum Attack)
print(group['Attack'].min())