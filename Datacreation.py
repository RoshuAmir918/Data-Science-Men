import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import os
import random
import seaborn as sns
from datetime import date

df = pd.read_csv(os.path.abspath(os.getcwd()) + "/Data-Science-Men/atlantic_refined.csv")
out = pd.DataFrame(columns = ["Landfall", "Days", "MaxWind", "MinWind", "AWind"])

def getDate(inp):
    year = int(str(inp)[:4])
    month = int(inp / 100) % 100
    day = inp % 100
    return date(year, month, day)



currentWind = []
currentP = []
startDate = getDate(df["Date"].iloc[0])
landfall = 1
currentId = df["ID"].iloc[0]

for ide, dateI, event, wind in zip(df["ID"], df["Date"], df["Event"], df["Maximum Wind"]):
    if ide != currentId:
        endDate = getDate(dateI)
        delta = endDate - startDate
        days = delta.days
        maxW = np.max(currentWind)
        minW = np.min(currentWind)
        avgW = np.average(currentWind)

        
        row = [landfall, days, maxW, minW, avgW]


        currentId = ide
        startDate = getDate(dateI)
        landfall = 0
        currentWind = []
        out.loc[len(out.index)] = row
    currentWind.append(wind)

    if(event == " L"):
        landfall = 1


out.to_csv(os.path.abspath(os.getcwd()) + "/Data-Science-Men/processed.csv")
        
        
        
