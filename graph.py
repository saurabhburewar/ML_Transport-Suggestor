"""
The function for building the graph from the given 
data is defined here
The graph is saved as a png file for viewing later

"""

import util
import csv
import networkx as nx
import matplotlib.pyplot as plt
import os

roadG = nx.Graph()
roadGpos = nx.spring_layout(roadG)
airG = nx.Graph()
labels = {}

def buildRoadGraph():
    with open("Data/RoadData.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            node1 = row[0]
            node2 = row[1]
            cost = int(row[2])
            roadG.add_edge(node1, node2, weight=cost)
            labels[node1] = node1
            labels[node2] = node2

    nx.draw(roadG)
    if (os.path.isdir("Graphs") == False):
        os.mkdir("Graphs")
    # nx.draw_networkx_labels(roadG, roadGpos, labels)
    plt.savefig("Graphs/RoadGraph.png")

def buildAirGraph():
    with open("Data/AirData.csv", "r") as csvFile:
        csvReader = csv.reader(csvFile)
        for row in csvReader:
            node1 = row[0]
            node2 = row[1]
            cost = int(row[2])
            airG.add_edge(node1, node2, weight=cost)

    nx.draw(airG)
    if (os.path.isdir("Graphs") == False):
        os.mkdir("Graphs")
    plt.savefig("Graphs/AirGraph.png")

def main():
    print("Airways graph (Heuristics): 0")
    print("Roadways graph (costs): 1")
    print()
    g = int(input("Answer: ").strip())

    if g == 0:
        buildAirGraph()
    elif g == 1:
        buildRoadGraph()
    

if __name__ == "__main__":
    main()
