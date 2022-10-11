import pandas as pd 
df = pd.read_csv("atlantic_open_refined.csv")

test = df[df["Name"] == "KATE"]

print(test[0:7])