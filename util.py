"""
All the supporting classes and functions, that are 
required for the project are defined here

"""

import heapq
import csv
import os

class PriorityQueue:

    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item
    
    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        for index, (p, c, i) in enumerate(self.heap):
            if (i == item):
                if (p <= priority):
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)


class Node:
    def __init__(self, node, cost):
        self.city = str(node)
        self.distance = str(cost)

"""
The distance between one city to another by air is taken
as the heuristic. 
Here, "heuristic" gives the distance between node1 and node2

Each row denotes the heuristic of node1, if node2 is the 
destination

"""
def getHeuristicDict(destination):
    hDict = {}
    with open("Data/AirData.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            node1 = str(row[0])
            node2 = str(row[1])
            if(node1 == destination):
                heuristic = int(row[2])
                hDict[node2] = heuristic
            if(node2 == destination):
                heuristic = int(row[2])
                hDict[node1] = heuristic

    return hDict


def getHeuristic(node, values):
    return values[node]


def getNodeDict():
    nodeDict = {}
    with open("Data/RoadData.csv", "r") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            node1 = row[0]
            node2 = row[1]
            cost = int(row[2])
            nodeDict.setdefault(node1, []).append(Node(node2, cost))
            nodeDict.setdefault(node2, []).append(Node(node1, cost))

    return nodeDict


def Write(lists):
    with open("./Data/LastSearchData.csv", "a+") as csvfile:
        csvWriter = csv.writer(csvfile)
        for row in lists:
            csvWriter.writerow(row)

def Createcsv():
    path = "./Data/LastSearchData.csv"
    if os.path.isfile(path):
        os.remove(path)
    heads = [["Mode", "Cost", "CO2_Emission"]]
    with open("./Data/LastSearchData.csv", "a+") as csvfile:
        writer = csv.writer(csvfile)
        for row in heads:
            writer.writerow(row)


