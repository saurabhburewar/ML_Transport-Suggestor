import csv
import util

RailDict = {}

def getRailDetails(src, dst):
    with open("Data/RailData.csv") as railfile:
        reader = csv.reader(railfile)
        for row in reader:
            node1 = row[0]
            node2 = row[1]
            if((node1 == src and node2 == dst) or (node1 == dst and node2 == src)):
                RailDist = int(row[2])
                RailCost = int(row[3])

    RailDict['cost'] = RailCost
    RailDict['distance'] = RailDist
    RailDict['carbonFp'] = RailDist*0.007837

    output(src, dst)
    UpdateCsv()

"""
The CO2 emission per passenger-km for Indian railways is 0.007837 kg
Source: https://www.linkedin.com/pulse/indian-railways-carbon-emission-debi-prasad-dash?articleId=6620101610364338176

"""

def output(src, dst):
    print("__________________________________________________________________________________________")
    print()
    print(src + " => " + dst + " (Rail Travel)")
    print("=======================================================")
    print("Estimate Cost \t: Rs. " + str(RailDict['cost']))
    print("Estimated CO2 emission \t: " + str(RailDict['carbonFp']) + " kg")
    print()
    print("__________________________________________________________________________________________")

def UpdateCsv():
    Uplist = []
    Uplist.append(["Rail", RailDict['cost'], RailDict['carbonFp']])
    util.Write(list(Uplist))