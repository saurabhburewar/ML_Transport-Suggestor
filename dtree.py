import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import pydotplus as pyd
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

def predictDtree(dist, envC, budgetC, avoid):
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

    classifier = DecisionTreeClassifier(criterion="gini")
    classifier = classifier.fit(X, Y)
    # data = tree.export_graphviz(classifier, out_file=None, feature_names=['Distance', 'Env_conscious', 'Budget_conscious', 'Avoid'])
    # dtree = pyd.graph_from_dot_data(data)
    # dtree.write_png("dtree.png")

    prediction = classifier.predict([[dist, envC, budgetC, avoid]])
    
    if prediction == 0:
        print("I think you should take the roads. The path I suggest is given above.")
    if prediction == 1:
        print("I think you should take a flight.")
    if prediction == 2:
        print("I think you should take a train.")