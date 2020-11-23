"""
The path searching function needed to calculate
the path and cost from one city to the other by 
road is defined here

"""
import util

def aStar(start, end, order):
    path = {}
    distance = {}
    pQueue = util.PriorityQueue()
    heuristic = util.getHeuristicDict(end)
    nodes = util.getNodeDict()

    pQueue.push(start, 0)
    distance[start] = 0
    path[start] = None
    visited = []

    while(pQueue.isEmpty() == False):
        current = pQueue.pop()
        visited.append(current)

        # Destination city is reached
        if(current == end):
            break

        for next in nodes[current]:
            gcost = distance[current] + int(next.distance)

            if(next.city not in distance or gcost < distance[next.city]):
                distance[next.city] = gcost
                fcost = gcost + util.getHeuristic(next.city, heuristic)
                pQueue.push(next.city, fcost)
                path[next.city] = current

    finalpath = []
    i = end
    while(path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()

    if order == "CheckHeuristic":
        details = [distance, heuristic, finalpath]
        return details

    if order == "PrintDetails":
        output(start, end, path, distance, visited, finalpath)
        return int(distance.get(end))

def output(start, end, path, distance, visited, finalpath):
    
    print("__________________________________________________________________________________________")
    print()
    print(start + " => " + end + " (Road Travel)")
    print("=======================================================")
    print("Cities you can explore on the way \t: " + str(visited))
    print("Number of cities that can be explored \t: " + str(len(visited)))
    print("=======================================================")
    print("The path I suggest you take is \t: " + str(finalpath))
    print("Number of cities passed \t: " + str(len(finalpath)))
    print("=======================================================")
    print("Total distance \t\t: " + str(distance.get(end)) + " km")

    """
    The average milleage of a vehicle in India is around 25kmpl and 
    the cost of gasoline is around Rs. 84, so the total cost in terms 
    of gasoline is given below
    For other possible miscellaneous costs for the road trip, we consider 
    an extra amount of Rs. (3*TotalDistance)

    """

    TotalDist = distance.get(end)
    TotalCost = (TotalDist/25)*84 + TotalDist*3
    TotalCost = "{:.2f}".format(TotalCost)
    print("Cost estimate \t\t: Rs. " + str(TotalCost))

    """
    The average carbon footprint or CO2 emissions by vehicles is recorded 
    to be somewhere 121 g/km in India
    Source: https://theicct.org/sites/default/files/publications/India_fuel_consumption_standards_20180925.pdf

    """
    carbonFp = (TotalDist * 121)/1000
    carbonFp = "{:.2f}".format(carbonFp)
    print("Estimated CO2 emission \t: " + str(carbonFp) + " kg")

    UpdateCsv(TotalCost, carbonFp)

def UpdateCsv(TotalCost, carbonFp):
    Uplist = []
    Uplist.append(["Road", TotalCost, carbonFp])
    util.Write(list(Uplist))

