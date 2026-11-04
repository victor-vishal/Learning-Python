import pandas as pd
#series is a 1D array or 1d labeled column that can hold any data type
# it can be thought of as a single column of a spreadsheet

data = [1,2,3,4,5]

series = pd.Series(data) # Series is a constructor and not a function (Capital S)
print(series) #prints the series with index and values
# it also prints data type of series as"dtype: int64"
# if any element is of float value then whole series will be float
# similarly if any element is of string value then dtype will be object
#the dtype is object when the series contains string/boolean values or a mix of data types.


#for better understanding we can even modify the index of series
series = pd.Series(data, index=['a','b','c','d','e']) # we can even pass another list as index
print(series)

#to access an element we use loc() method and pass the index value of that element
#Syntax: series.loc[index_value]
print(series.loc["a"])
# the values can also be updated using loc() method
series.loc["a"] = 100
print(series) # now the value of index "a" is updated to 100

# access can be also be done using integer position using iloc() method
#Syntax: series.iloc[position]
print(series.iloc[0]) # prints the value of first element in series


#filter by values
print(series[series>3])

#using dictionary
cal = {
    "Day1": 420,
    "Day2": 380,
    "Day3": 500,
    "Day5": 300
}

series = pd.Series(cal)
print(series)
# When series are created using dictionary, the keys become the index in pandas series
print(series.iloc[0])
series.iloc[3] = 1000 #using iloc() method to update the value at Day5 index
print(series)

print(series.index[series>400]) #prints index values of series satisfying the condition
#Index(['Day1', 'Day3', 'Day5'], dtype='str')
print(series[series>400])