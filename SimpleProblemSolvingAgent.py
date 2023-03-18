import math
import heapq
import random
import sys


def print_path(path):  # Custom path output formatting
    print("Path: ", end="")

    for i in range(0, len(path) - 1):
        print(path[i], end=" -> ")
    print(path[-1])


class SimpleProblemSolvingAgent:
    """Initializes a SimpleProblemSolvingAgent (SPSA) Object.

    :param map_graph: Undirected Graph representing the given map of Romania
    :param map_locations: Dictionary containing the Cartesian coordinates of cities on the Romania map
    :param start: The given start city
    :param goal: The Destination city
    :returns: None
    """
    def __init__(self, map_graph, map_locations, start, goal):
        self.map_Graph = map_graph
        self.map_locations = map_locations
        self.start = start
        self.goal = goal

    """Wrapper method for calling a specified traversal algorithm.
    
    :param search_type: The algorithm to use
    """
    def search(self, search_type):
        if search_type == "Greedy Best First Search" or search_type == "A* Search":
            self.heap_searches(search_type)
        elif search_type == "Hill-Climbing":
            self.hill_climbing_search()
        elif search_type == "Simulated Annealing":
            self.simulated_annealing_search()

    """Can perform both Greedy Best First Search and A* Search.
    
    Both of these algorithms utilize a heap to keep track of the 'optimal' path.
    
    :param search_type: The algorithm to be performed
    :returns: void
    """
    def heap_searches(self, search_type):
        paths_list = [(0, self.start, [self.start])]  # Keep track of paths
        visited_cities = set()  # Keep track of visited cities

        while paths_list:
            (weight, currCity, path) = heapq.heappop(paths_list)  # Get the lowest weighted path

            if currCity not in visited_cities:  # New city
                visited_cities.add(currCity)
            else:  # Already visited
                continue

            if currCity == self.goal:  # Destination city has been reached
                self.print_results(path)
                return

            for neighbor in self.map_Graph.get(currCity).keys():  # Get the current city's neighbors
                if search_type == "Greedy Best First Search":
                    weight = self.straight_line_heuristic(neighbor, self.goal)  # h(n)
                elif search_type == "A* Search":
                    weight = self.straight_line_heuristic(self.start, neighbor) + self.straight_line_heuristic(neighbor, self.goal)  # g(n) + h(n)
                heapq.heappush(paths_list, (weight, neighbor, path + [neighbor]))  # Push updated path back into heap
        return None

    """Performs the Hill-Climbing search in order to find a solution path.
    
    This variant of the Hill-Climbing algorithm utilizes a greedy local search, where it will move to the neighbor that
    has the shortest straight line distance to the goal city. 

    :returns: void
    """
    def hill_climbing_search(self):
        path = [self.start]  # Keep track of path
        currCity = path[0]
        lowest_cost = self.straight_line_heuristic(self.start, self.goal)

        while True:
            neighbors = self.map_Graph.get(currCity).keys()  # Get the current city's neighbors

            if not neighbors:
                break

            best_neighbor = None

            # Find the closest neighbor to the destination city
            for neighbor in neighbors:
                neighbor_cost = self.straight_line_heuristic(neighbor, self.goal)

                # Move to the neighbor closest to the goal city that isn't already on the current path
                if neighbor_cost < lowest_cost and neighbor not in path:
                    lowest_cost = neighbor_cost
                    best_neighbor = neighbor

            if best_neighbor is None:  # Hit a local minima
                break

            path += [best_neighbor]
            currCity = best_neighbor  # Set the neighbor as the next city to be expanded upon

        self.print_results(path)
        return None

    """Exponential Multiplicative Cooling scheduling variant helper method for the Simulated Annealing algorithm.
    
    Stopped using this because 'math.exp(delta_e / T)' in probability() kept getting OverFlow errors.
    
    :param init_temp: The initial temperature
    :param cooling_rate: The rate at which the temperature is cooled
    :returns: The temperature after t iterations has passed
    """
    def exp_schedule(self, init_temp=1000, cooling_rate=0.95):
        return lambda t: init_temp * (cooling_rate ** t)

    """Logarithmical Multiplicative Cooling scheduling variant helper method for the Simulated Annealing algorithm.

    :param init_temp: The initial temperature
    :param cooling_rate: The rate at which the temperature is cooled
    :returns: The temperature after t iterations has passed
    """
    def log_schedule(self, init_temp=10000, cooling_rate=1000):
        return lambda t: init_temp / (1 + (cooling_rate * math.log(1 + t)))

    """Probability helper method for the Simulated Annealing algorithm.
    
    :param delta_e: The difference in cost between the chosen neighboring city and the current city
    :param T: The temperature in the given iteration
    :returns: a boolean representing the probability of true
    """
    def probability(self, delta_e, T):
        return math.exp(delta_e / T) > random.uniform(0.0, 1.0)

    """Performs the Simulated Annealing search in order to find a solution path.
    
    :returns: void
    """
    def simulated_annealing_search(self):
        path = [self.start]  # Keep track of path
        currCity = self.start

        for t in range(sys.maxsize):
            T = self.log_schedule()(t)

            if T == 0:
                break

            if currCity == self.goal:  # Destination city has been reached
                break

            neighbors = list(self.map_Graph.get(currCity).keys())  # Get the current city's neighbors as a list

            if not neighbors:
                break

            nextCity = random.choice(neighbors)

            delta_e = self.manhattan_heuristic(nextCity, self.goal) - self.manhattan_heuristic(currCity, self.goal)

            if delta_e < 0 or self.probability(delta_e, T):
                path += [nextCity]
                currCity = nextCity

        self.print_results(path)
        return None

    """Calculates the straight-line distance from the current city to the goal city.

    :param currCity: The given start city
    :param goal: The given destination city
    :returns: The straight-line distance between the given cities.
    """
    def straight_line_heuristic(self, currCity, goal):
        x1 = self.map_locations[currCity][0]
        y1 = self.map_locations[currCity][1]
        x2 = self.map_locations[goal][0]
        y2 = self.map_locations[goal][1]
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))  # Pythagorean Theorem

    """Calculates the manhattan distance from the current city to the goal city.
    
    This heuristic is mainly implemented for the Simulated Annealing algorithm, as it seems to provide better results
    as compared to the straight-line heuristic. This could be due to it better representing movement in a grid-like
    environment.
    
    :param currCity: The given start city
    :param goal: The given destination city
    :returns: The manhattan distance between the given cities.
    """
    def manhattan_heuristic(self, currCity, goal):
        x1 = self.map_locations[currCity][0]
        y1 = self.map_locations[currCity][1]
        x2 = self.map_locations[goal][0]
        y2 = self.map_locations[goal][1]
        return abs(x2 - x1) + abs(y2 - y1)

    """Calculates the given path's distance
    
    :param path: An array representing the path
    :return: The total distance traveled
    """
    def calculate_path_cost(self, path):
        cost = 0

        for i in range(0, len(path) - 1):
            cost += self.map_Graph.get(path[i], path[i + 1])
        return cost

    """Helper method for printing the results of a search traversal algorithm
    """
    def print_results(self, path):
        print("Total Cost is: " + str(self.calculate_path_cost(path)))
        print_path(path)
