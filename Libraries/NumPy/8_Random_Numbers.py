import numpy as np

rng = np.random.default_rng(seed=1) #passing seed value is optional, it makes the output of random numbers reproducible,
#default_rng() is the recommended constructor for creating a new Generator object
# after passing seed value, same random numbers will be generated everytime code is ran
print(rng.integers(low=1, high=101, size=3)) #3 ints between 1 to 100 in 1D array
print()
print(rng.integers(1, 101, (3,2))) # size = 3,2 means 6 elements in 2d array of 3 rows and 2 columns
print("\n\n")


#to set Seed:
np.random.seed(seed=1)
#Syntax: np.random.uniform(loq, high, size)
print(np.random.uniform(low=-1, high=1)) # uniform distribution, meaning all numbers within the range have equal probability of being selected, low and high default to 0 and 1 respectively, if not specified
#generate 6 random numbers in a 3x2 array between -1 and 1
print(np.random.uniform(low=-1, high=1, size=(3,2)))

#Shuffling an array: we use rng.shuffle()
rng = np.random.default_rng()# we can pass a seed value to make the shuffling reproducible
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array) # shuffles the original array without creating a new array

fruits = np.array(['apple', 'cherry', 'mango', 'grapes'])
print("Before shuffling:", fruits)
rng.shuffle(fruits)
print("After Shuffling:", fruits)
# we can randomly select shuffled elements from array using choice() function
fruit = rng.choice(fruits, size=3) #returns 3 random elements from the passed array(that is already shuffled)
print("After selecting 3 elements from a shuffled array:", fruit)

#using emojis instead of strings
fruits = np.array(['🍎', '🍒', '🥭', '🍇'])
rng.shuffle(fruits)
print(rng.choice(fruits, size=(3,3)))