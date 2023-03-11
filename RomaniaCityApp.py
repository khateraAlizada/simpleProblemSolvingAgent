from SimpleProblemSolvingAgent import SimpleProblemSolvingAgent
import Graph
import json


def main():
    response = ""
    while True:
        file_path = input("Enter the map file location\n> ")  # Local path to map file is 'romania_map.json'

        try:
            with open(file_path, "r") as f:
                state = json.loads(f.read())
                break
        except FileNotFoundError:
            print("Could not find the file")

    while response != "No":
        start = input("Enter starting city.\n> ").title()
        if start not in state["locations"]:
            print("Could not find the city on the map, start again..")
            continue
        goal = input("Enter ending city.\n> ").title()
        if goal not in state["locations"]:
            print("Could not find the city on the map, start again..")
            continue
        if start == goal:
            print("Start and end cities are the same, start again..")
            continue

        romania_graph = state["romaniaMap"]
        undirected_romania_map = Graph.UndirectedGraph(romania_graph)

        romania_map_locations = state["locations"]

        print("\nCalculating path from " + start + " to " + goal + ".\n")
        solver = SimpleProblemSolvingAgent(undirected_romania_map, romania_map_locations, start, goal)
        print("Utilizing Greedy Best-First Search:")
        solver.search("Greedy Best First Search")
        print("\nUtilizing A* Search:")
        solver.search("A* Search")
        print("\nUtilizing Hill-Climbing Search")
        solver.search("Hill-Climbing")
        print("\nUtilizing Simulated Annealing Search")
        solver.search("Simulated Annealing")

        response = input("Would you like to calculate a new path? ('Yes' or 'No').\n> ").title()
        print(response)

    print("Thank you for using our app!")


if __name__ == "__main__":
    main()
