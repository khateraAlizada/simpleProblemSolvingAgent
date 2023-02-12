from SimpleProblemSolvingAgent import SimpleProblemSolvingAgent
import Graph
import json

# TODO: Figure out how to read in the romania_map.txt file; temporarily hardcode Dictonarys for now
romania_graph = dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142))

romania_map_locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))

unDirRomaniaMap = Graph.UndirectedGraph(romania_graph)


def main():
    # TODO: (High Prio!!!) -> Need to prompt user to input where map_file is, then read in romania_map and romania_map.locations
    # TODO: Add error handling for invalid input
    response = ""

    while response != "No":
        start = input("Enter starting city.\n> ").title()
        goal = input("Enter destination city.\n> ").title()

        print("\nCalculating path from " + start + " to " + goal + ".\n")

        solver = SimpleProblemSolvingAgent(unDirRomaniaMap, romania_map_locations, start, goal)
        print("Utilizing Greedy Best-First Search:")
        solver.search("Greedy Best First Search")
        print("\nUtilizing A* Search:")
        solver.search("A* Search")

        response = input("Would you like to calculate a new path? ('Yes' or 'No').\n> ")

    print("Thank you for using our app!")


if __name__ == "__main__":
    main()
