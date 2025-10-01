import pandas as pd

# Load file
df = pd.read_csv("car_fuel_efficiency.csv")

# Q1
print("Q1:", pd.__version__)

# Q2
print("Q2:", len(df))

# Q3
print("Q3:", df["fuel_type"].nunique())

# Q4
print("Q4:", (df.isnull().sum() > 0).sum())

# Q5
print("Q5:", round(df["fuel_efficiency_mpg"].max() * 4) / 4)

# Q6 (conventional if/else style)
medianHpByYear = df.groupby("model_year")["horsepower"].median()
if medianHpByYear.iloc[-1] > medianHpByYear.iloc[0]:
    print("Q6: Yes, it increased")
elif medianHpByYear.iloc[-1] < medianHpByYear.iloc[0]:
    print("Q6: Yes, it decreased")
else:
    print("Q6: No")

# Q7
print("Q7:", round(df["vehicle_weight"].sum() / 1e6, 2))
