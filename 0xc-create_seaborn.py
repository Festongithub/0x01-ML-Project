#!/usr/bin/python3

import seaborn as sns
import matplotlib.pyplot as plt
#Apply the default theme
sns.set_theme()

#Load an example dataset
data =sns.load_dataset("iris")
# plot for the data
sns.lineplot(x="sepal_length", y="sepal_width", data=data)
# Title for the measurement
plt.title("Nature Measurement")
# cahnging the figure size
#plt.figure(figsize = (2, 4))
#setting the limit of the plot
plt.xlim(0)
# setting y limit of the plot
plt.ylim(0)
#set style for the graph
sns.set_style("dark")
# removing the spine
sns.despine()
# setting scale of the plot
sns.set_context("paper")
# show()
plt.show()

