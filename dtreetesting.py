import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import matplotlib.image as pltimg


def main():
    df = pd.read_csv("Data/dTreeData.csv")

    # All Data should be numerical to make decision tree
    d = {'Yes': 1, 'No': 0}
    df['Env_conscious'] = df['Env_conscious'].map(d)
    df['Budget_conscious'] = df['Budget_conscious'].map(d)

    d = {'Road': 0, 'Air': 1, 'Rail': 2}
    df['Avoid'] = df['Avoid'].map(d)
    df['Mode'] = df['Mode'].map(d)

    X = df[['Distance', 'Env_conscious', 'Budget_conscious', 'Avoid']]
    Y = df['Mode']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 100)

    # Gini classifier
    giniClassifier = giniTrain(X_train, Y_train, X_test)
    giniPredic = giniClassifier.predict(X_test)
    print("Predicted Values (gini): ")
    print(giniPredic)
    calAccuracy(Y_test, giniPredic)

    # Entropy classifier
    # entropyClassifier = entropyTrain(X_train, Y_train, X_test)
    # entropyPredic = entropyClassifier.predict(X_test)
    # print("Predicted Values (entropy): ")
    # print(entropyPredic)
    # calAccuracy(Y_test, entropyPredic)

def giniTrain(X_train, Y_train, X_test):    
    giniClassifier = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=3, min_samples_leaf=5)
    giniClassifier.fit(X_train, Y_train)
    return giniClassifier

def entropyTrain(X_train, Y_train, X_test):
    entropyClassifier = DecisionTreeClassifier(criterion="entropy", random_state=100, max_depth=3, min_samples_leaf=5)
    entropyClassifier.fit(X_train, Y_train)
    return entropyClassifier

def calAccuracy(Y_test, predic):
    print("Accuracy: " + str(accuracy_score(Y_test, predic)*100) + " %")
    print("Report: " + classification_report(Y_test, predic))

if __name__ == "__main__":
    main()