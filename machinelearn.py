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
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier



def graphIt(X_train, X_test, y_train, y_test):
    pca = PCA(n_components = 2)
    pca.fit(X_train)
    X_train2D = pca.transform(X_train)
    X_test2D = pca.transform(X_test)

    f, axarr = plt.subplots(1, 2, sharex='col', sharey='row', figsize=(10, 5))
    for i in range(2):
        axarr[0].scatter(X_train2D[y_train == i, 0], X_train2D[y_train == i, 1], label = str(i))
                                        
        axarr[0].legend()
        axarr[0].set_title('Training data')

        axarr[1].scatter(X_test2D[y_test == i, 0], X_test2D[y_test == i, 1], label = str(i))
                                        
        axarr[1].legend()
        axarr[1].set_title('Testing data')
    plt.show()




df = pd.read_csv(os.path.abspath(os.getcwd()) + "/Data-Science-Men/processed.csv")
#df = pd.concat([df, pd.get_dummies(df["Landfall"])], axis = 1).drop(columns = ["Landfall"])


X = df.drop(columns = ["Landfall"])
y = df["Landfall"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle = True)

scaler = StandardScaler()  
scaler.fit(X_train)  
X_train = scaler.transform(X_train)  

X_test = scaler.transform(X_test)

#graphIt(X_train, X_test, y_train, y_test)

logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)

predictions = logmodel.predict(X_test)



nn = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(3, 5), random_state=5)

nn.fit(X_train, y_train)

print('Training accuracy: ', nn.score(X_train, y_train))
print('Testing accuracy: ', nn.score(X_test, y_test))


