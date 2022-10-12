import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv("atlantic2.csv")
img = plt.imread("oceanmap.png")




conditions = [
    (df["Date"] <= 19000000),
    (df["Date"] > 19000000) & (df["Date"] <= 19300000),
    (df["Date"] > 19300000) & (df["Date"] <= 19600000),
    (df["Date"] > 19600000) & (df["Date"] <= 20000000),
    (df["Date"] > 20000000)
    ]
values = ["Cyan", "Green", "Khaki", "Darkorange", "Red"]
df["Named"] = np.select(conditions, values)
df["Size"] = np.where(df["Name"] != "UNNAMED", 2, .5)

latitude = df["Latitude"]
longitude = df["Longitude"]

#plt.imshow(img)
plt.xlim(-120, 0)
plt.ylim(0, 45)
plt.scatter(longitude, latitude, s = df["Size"], c = df["Named"])
plt.show()