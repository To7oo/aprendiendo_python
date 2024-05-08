import pandas as pd
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
#print(df["Sex"])

ages = pd.Series([22, 35, 58], name="Age")

#print(ages)

#print(df["Age"].max())

#print(df.describe())

titanic = pd.read_csv("titanic.csv")

print(titanic.head())

#print(titanic.dtypes)

#titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
#titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
#titanic.head()


#print(titanic)

#print(titanic.info())

ages = titanic["Age"]

type(titanic["Age"])

#print(titanic["Age"].shape)

age_sex = titanic[["Age", "Sex"]]

#print(age_sex.head())

above_35 = titanic[titanic["Age"] > 35]

titanic["Age"] > 35

#print(titanic)
print(above_35.shape)