import seaborn as sns
diamond=sns.load_dataset("diamonds")

sns.distplot(diamond["price"],diamond["x"])
