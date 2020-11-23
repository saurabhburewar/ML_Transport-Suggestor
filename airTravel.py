import csv
import util

FlightDict = {}


def getAirDetails(src, dst):
    with open("Data/AirData.csv") as airfile:
        reader = csv.reader(airfile)
        for row in reader:
            node1 = row[0]
            node2 = row[1]
            if((node1 == src and node2 == dst) or (node1 == dst and node2 == src)):
                FlightDist = int(row[2])
                FlightCost = int(row[3])

    """
    The average CO2 emssions of a Boeing 737 is 115 g per passenger-km
    Source: https://www.carbonindependent.org/22.html

    """
    
    FlightDict['carbonFp'] = (FlightDist*115)/1000
    FlightDict['cost'] = FlightCost

    output(src, dst)
    UpdateCsv()
    
def output(src, dst):
    print("__________________________________________________________________________________________")
    print()
    print(src + " => " + dst + " (Air Travel)")
    print("=======================================================")
    print("Estimate Cost \t: Rs. " + str(FlightDict['cost']))
    print("Estimated CO2 emission \t: " + str(FlightDict['carbonFp']) + " kg")
    print()

def UpdateCsv():
    Uplist = []
    Uplist.append(["Air", FlightDict['cost'], FlightDict['carbonFp']])
    util.Write(list(Uplist))