import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import os
import random
import seaborn as sns
from datetime import date
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA



df = pd.read_csv(os.path.abspath(os.getcwd()) + "/Data-Science-Men/processed.csv")
#df = pd.concat([df, pd.get_dummies(df["Landfall"])], axis = 1).drop(columns = ["Landfall"])


X = df.drop(columns = ["Landfall"])
Y = df["Landfall"]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, shuffle = True)

scaler = StandardScaler()  
scaler.fit(X_train)  
X_train = scaler.transform(X_train)  

X_test = scaler.transform(X_test)


pca = PCA(n_components = 2)
pca.fit(X_train)
X_train2D = pca.transform(X_train)
X_test2D = pca.transform(X_test)




