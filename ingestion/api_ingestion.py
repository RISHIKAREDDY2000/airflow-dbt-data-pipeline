import pandas as pd

df = pd.read_csv("datasets/api_sales_sample.csv")

df.to_csv("/tmp/raw_sales.csv", index=False)

print("Data ingested successfully")
