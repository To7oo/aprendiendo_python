import pandas as pd

df = pd.read_csv('./customers/titanic.csv', sep=',')

adult_names = df.loc[df["Age"] > 35, "Name"]

print(adult_names)