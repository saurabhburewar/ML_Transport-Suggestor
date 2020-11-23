import csv
import search
import util

def isadmissible():
    with open("./Data/RoadData.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            start = row[0]
            end = row[1]
            details = search.aStar(start, end, "CheckHeuristic")
            
            if details[0].get(end) >= util.getHeuristic(start, details[1]):
                adm = True
            else:
                adm = False
        
    print("Admissible: " + str(adm))

def isConsistent():
    with open("./Data/RoadData.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            start = row[0]
            end = row[1]
            details = search.aStar(start, end, "CheckHeuristic")
            finalpath = details[2]
            distance = details[0]
            for i in range(len(details[2]) - 1):
                if distance[finalpath[i+1]] - distance[finalpath[i]] >= util.getHeuristic(finalpath[i+1], details[1]) - util.getHeuristic(finalpath[i], details[1]):
                    cons = True
                else:
                    cons = False
                    break
    
    print("Consistent: " + str(cons))

            
if __name__ == "__main__":
    isadmissible()
    isConsistent()