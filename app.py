import pandas as pd
import csv
df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

df = pd.concat([df0, df1, df2])
df = df[df["product"] == "pink morsel"]
df['price'] = df['price'].str[1:].astype(float)
df["sales"] = df["quantity"] * df["quantity"]
df.drop(columns=["price", "quantity", "product"], axis=1, inplace=True)

df.to_csv("formatted.csv", index=False)
