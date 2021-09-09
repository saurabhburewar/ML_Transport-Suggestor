# Transport Suggester

An CLI application that suggests a mode of transport and route in terms of cities passed by taking inputs on source, destination and other preferences like cost of trip, environment-friendly. It uses a simple decision tree classifier to make the decision on the mode of transport.

## Requirements

Python 3.6 and above  
Modules - sklearn, matplotlib, networkx

## Application

To open the application, run the file **main.py** through cmd/terminal.
Enter the inputs as asked by the application

The output is displayed in the terminal.

> python main.py

Files included in main application are -
- main.py
- util.py
- search.py
- airTravel.py
- railTravel.py
- dtree.py


## Additional modules

These are some additional modules that can be executed seperately for additional information regarding the components of the project.

### dtreetesting.py

You can run this module to test the decision tree and it's properties. It divides the data in 70:30 ratio of training and testing and returns the test outputs with accuracy od decisions. 

> python dtreetesting.py

### checkHeuristic.py

You can run this module seperately to check if the heuristic applied is admissible and consistent. 
It returns True or False for the respective properties.

> python checkHeuristic.py

### graph.py

You can run this module seperately to save the required graph in PNG format.

> python graph.py

Graphs are saved in the directory "Graphs" in the root.

## Dataset

The datasets are stored in the directory "Data" in the root.

These include -
- AirData.csv
- RailData.csv
- RoadData.csv
- dTreeData.csv

## Files you can ignore

- Directory "Files not in use"
