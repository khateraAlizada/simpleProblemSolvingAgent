
def main():
    file_path = input("Enter the map file location: ")

    with open(file_path, "r") as file:
        map = file.read()

    # romania_map = {}

    print("Romania map: " + "\n" + map)


    # import importlib.util
    # import sys
    # spec = importlib.util.spec_from_file_location("romania_map", file_path)
    # romania_map = importlib.util.module_from_spec(spec)
    # sys.modules["romania_map"] = romania_map
    # spec.loader.exec_module(romania_map)

    # spec = importlib.util.spec_from_file_location("romania_map.locations", file_path)
    # romania_map.locations = importlib.util.module_from_spec(spec)
    # sys.modules["romania_map.locations"] = romania_map.locations
    # spec.loader.exec_module(romania_map.locations)

    # parse the map data and populate romania_map and locations
    # romania_map = romania_map.romania_map
    # print("Map data: ", romania_map)
    # print("Locations: ", romania_map.locations)

    # while True:
    #     city1 = input("Enter the first city: ")
    #     city2 = input("Enter the second city: ")
    #
    #     if city1 == city2:
    #         print("Both cities are the same. Please enter different cities.")
    #     elif city1 not in romania_map or city2 not in romania_map:
    #         print("One or both cities are not in the Romania map. Please enter valid cities.")
    #     else:
    #         break
    # while True:
        # Step b and c
        # ...

        # Ask the user if they want to repeat
        # repeat = input("Do you want to find the best path between two cities again? (yes/no)")
        # if repeat.lower() == "no":
        #     print("Thank you for using our app.")
        #     break

    from search import SimpleProblemSolvingAgentProgram
    from search import greedy_best_first_graph_search
    from search import astar_search

    # User input for start and end cities
    start_city = input("Enter the start city: ")
    end_city = input("Enter the end city: ")

    # Create a SPSA object
    agent = SimpleProblemSolvingAgentProgram(start_city, end_city)

    # Perform GBFS and A* searches
    gbfs_result = greedy_best_first_graph_search(agent.romania_map, start_city, end_city)
    astar_result = astar_search(agent.romania_map, start_city, end_city)

    # Output results for GBFS
    print("Search Method: Greedy Best-First Search")
    print("Total Cost: ", gbfs_result[0])
    print("Intermediate Cities: ", gbfs_result[1])

    # Output results for A*
    print("Search Method: A* Search")
    print("Total Cost: ", astar_result[0])
    print("Intermediate Cities: ", astar_result[1])


if __name__ == "__main__":
    main()
