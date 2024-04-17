#!/usr/bin/python3

import pandas as pd

data = pd.read_csv("nba.csv")
df = pd.DataFrame(data)

first = data["Age"]
print("{}".format(first))

row2 = data.iloc[3]
print(row2)
