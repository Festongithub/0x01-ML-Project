#!/usr/bin/python3

import pandas as pd
import numpy as np

data = {
        'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
        'City': ['Mexico City', 'Toronto', 'Prague', 'Shanghai', 'Manchester', 'Cairo',
                 'Osaka'],
        'age': [41, 28, 33, 34, 38, 31, 37],
        'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
        }

row_labels = [101, 102, 103, 104, 105, 106, 107]


df = pd.DataFrame(data=data, index=row_labels)
print(df)

for key, value in data.items():
    print(key, value)
print(df.name)
print(df.loc[102])


# creating pandas DataFrame with Dictionaries

l = list(range(10, 234))
print(pd.DataFrame(l, columns=['x']))

# using Numpy Arrays
product_array = np.array([l])

print("{}".format(product_array))

prod_a = pd.DataFrame(product_array)
print(prod_a)

# read from files
my_csv = pd.read_csv("nba.csv", index_col=0)
print(my_csv)
# get the number of rows
print(my_csv.index)
#get the number of columns

print(my_csv.columns[0])

new_csv = my_csv.to_numpy()
print(new_csv)

