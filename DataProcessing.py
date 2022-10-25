import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import os
import random
import seaborn as sns


def get_Colors(df):
    colors = []
    currentName = ""
    for name in df["Name"]:
        if name == "UNNAMED":
            colors.append((1, 1, 1))
        elif name == currentName:
            colors.append(colors[len(colors)-1])
        else: 
            colors.append((random.random(), random.random(), random.random()))
            currentName = name
    return colors

def boxPlot1(df):
    unNamed = []
    named = []
    beforeNaming = []
    currentIdWind = []
    currentId = df["ID"].iloc[0]
    for wind, iden, name, year in zip(df["Maximum Wind"], df["ID"], df["Name"], df["Date"]):
        if iden != currentId and wind != -99:
            currentId = iden
            if name == "UNNAMED" and year < 19530000:
                unNamed.append(np.max(currentIdWind))
            elif name != "UNNAMED" and year < 19530000:
                named.append(np.max(currentIdWind))
            else:
                beforeNaming.append(np.max(currentIdWind))
            currentIdWind = []
        currentIdWind.append(wind)
    return unNamed, named, beforeNaming


def strengthByQuarterCentury(df):
    startYear = 18750000
    periods = []
    current = []
    currentIdWind = []
    currentId = df["ID"].iloc[0]
    for wind, iden, year in zip(df["Maximum Wind"], df["ID"], df["Date"]):
        if iden != currentId and wind != -99:
            currentId = iden
            if year < startYear:
                current.append(np.max(currentIdWind))
            elif year >= startYear:
                startYear += 250000
                periods.append(current)
                current = []
            currentIdWind = []
        currentIdWind.append(wind)
    periods.append(current)
    return periods

def densityPlot(df):
    startYear = 19000000
    periods = []
    current = []
    currentIdWind = []
    currentId = df["ID"].iloc[0]
    for wind, iden, year in zip(df["Maximum Wind"], df["ID"], df["Date"]):
        if iden != currentId and wind != -99:
            currentId = iden
            if year < startYear:
                current.append(np.max(currentIdWind))
            elif year >= startYear:
                startYear += 500000
                periods.append(current)
                current = []
            currentIdWind = []
        currentIdWind.append(wind)
    periods.append(current)
    return periods

def timeByLandfall(df):
    times = []
    currentIdTime = []
    currentId = df["ID"].iloc[0]
    for iden, time in zip(df["ID"], df["Time"]):
        if iden != currentId:
            currentId = iden
            hours = 0
            for t in currentIdTime[1:-1]:
                if t == 0:
                    hours += 24
            if hours > 24:
                hours = hours - currentIdTime[0]/100
                hours = hours + currentIdTime[-1]/100
            times.append(hours)      
            currentIdTime = []
        currentIdTime.append(time)

    times.append(hours)
    return times

def timeIfLandfall(df):
    landfall = []
    noLandfall = []
    currentIdTime = []
    currentId = df["ID"].iloc[0]
    landfallBool = False
    for iden, time, event in zip(df["ID"], df["Time"], df["Event"]):
        if event == " L":
            landfallBool = True
        if iden != currentId:
            currentId = iden
            hours = 0
            for t in currentIdTime[1:-1]:
                if t == 0:
                    hours += 24
            if hours > 24:
                hours = hours - currentIdTime[0]/100
                hours = hours + currentIdTime[-1]/100
            if landfallBool == True:
                landfall.append(hours) 
            else:
                noLandfall.append(hours)     
            currentIdTime = []
            landfallBool = False
        currentIdTime.append(time)

    if landfallBool == True:
        landfall.append(hours)
    else:
        noLandfall.append(hours)
    return landfall, noLandfall




df = pd.read_csv(os.path.abspath(os.getcwd()) + "/Data-Science-Men/atlantic_refined.csv")
im = plt.imread(os.path.abspath(os.getcwd()) + "/Data-Science-Men/map.png")

longitude = df["Latitude"]
latitude = df["Longitude"]

colors = get_Colors(df)

unNamed, named, beforeNaming = boxPlot1(df)
qc = strengthByQuarterCentury(df)



fig, ax = plt.subplots()
columns = [beforeNaming, unNamed, named]
ax.set_title("Hurricanes Max Wind Speeds")
ax.boxplot(columns)
ax.set_xticklabels(["Before Naming", "Unnamed Hurricanes", "Named Hurricanes"])
plt.savefig(os.path.abspath(os.getcwd()) + "/Data-Science-Men/WindSpeed.png")


fig, ax1 = plt.subplots()
ax1.set_title("Hurricane Strength by Quarter Century")
ax1.boxplot(qc)
ax1.set_xticklabels(["1850", "1875", "1900", "1925", "1950", "1975", "2000"])
plt.savefig(os.path.abspath(os.getcwd()) + "/Data-Science-Men/WindSpeedYear.png")


fig, ax2 = plt.subplots()
plt.xlim(-115, 0)
plt.ylim(0, 70)
ax2.set_title("Hurricanes Graphed")
ax2.scatter(latitude, longitude, s = 3, c = colors)
implot = ax1.imshow(im, extent=[-115, 0, 0, 70])
plt.savefig(os.path.abspath(os.getcwd()) + "/Data-Science-Men/HurricaneMap.png", dpi = 180)

fig, ax3 = plt.subplots()
first, second, third, fourth = densityPlot(df)
sns.kdeplot(first, shade=True, color="g", label="1850-1900", alpha=.7)
sns.kdeplot(second, shade=True, color="deeppink", label="1900-1950", alpha=.7)
sns.kdeplot(third, shade=True, color="dodgerblue", label="1950-2000", alpha=.7)
sns.kdeplot(fourth, shade=True, color="orange", label="2000-2015", alpha=.7)
ax3.set_title("Density Plot of High Wind Speed by Half-Century", fontsize=10)
ax3.legend()
ax3.set_xlabel("Wind Speed (knots)")
plt.savefig(os.path.abspath(os.getcwd()) + "/Data-Science-Men/DensityYears.png", dpi = 180)


fig, ax4 = plt.subplots()
times = timeByLandfall(df)
sns.kdeplot(times, shade=True, color="magenta", alpha=.7)
ax4.set_title("Density Plot of Time of Storm", fontsize=10)
ax4.set_xlabel("Time (hours)")
plt.savefig(os.path.abspath(os.getcwd()) + "/Data-Science-Men/DensityHours.png", dpi = 180)


fig, ax5 = plt.subplots()
landfall, noLandfall = timeIfLandfall(df)
sns.kdeplot(landfall, shade=True, color="#54FF9F", label="Landfall", alpha=.7)
sns.kdeplot(noLandfall, shade=True, color="#4B0082", label="No Landfall", alpha=.7)
ax5.set_title("Density Plot of Times With and Without Landfall", fontsize=10)
ax5.legend()
ax5.set_xlabel("Time (hours)")
plt.savefig(os.path.abspath(os.getcwd()) + "/Data-Science-Men/DensityHoursLandfall.png", dpi = 180)
plt.show()






