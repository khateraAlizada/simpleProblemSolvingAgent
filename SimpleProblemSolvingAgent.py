from utils import *
import sys
from collections import deque


# ______________________________________________________________________________
# Graphs and Graph Problems


class Graph:
    """A graph connects nodes (vertices) by edges (links). Each edge can also
    have a length associated with it. The constructor call is something like:
        g = Graph({'A': {'B': 1, 'C': 2})
    this makes a graph with 3 nodes, A, B, and C, with an edge of length 1 from
    A to B,  and an edge of length 2 from A to C. You can also do:
        g = Graph({'A': {'B': 1, 'C': 2}, directed=False)
    This makes an undirected graph, so inverse links are also added. The graph
    stays undirected; if you add more links with g.connect('B', 'C', 3), then
    inverse link is also added. You can use g.nodes() to get a list of nodes,
    g.get('A') to get a dict of links out of A, and g.get('A', 'B') to get the
    length of the link from A to B. 'Lengths' can actually be any object at
    all, and nodes can be any hashable object."""

    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        """Make a digraph into an undirected graph by adding symmetric edges."""
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect1(b, a, dist)

    def connect(self, A, B, distance=1):
        """Add a link from A and B of given distance, and also add the inverse
        link if the graph is undirected."""
        self.connect1(A, B, distance)
        if not self.directed:
            self.connect1(B, A, distance)

    def connect1(self, A, B, distance):
        """Add a link from A to B of given distance, in one direction only."""
        self.graph_dict.setdefault(A, {})[B] = distance

    def get(self, a, b=None):
        """Return a link distance or a dict of {node: distance} entries.
        .get(a,b) returns the distance or None;
        .get(a) returns a dict of {node: distance} entries, possibly {}."""
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    def nodes(self):
        """Return a list of nodes in the graph."""
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)


def UndirectedGraph(graph_dict=None):
    """Build a Graph where every edge (including future ones) goes both ways."""
    return Graph(graph_dict=graph_dict, directed=False)


# ______________________________________________________________________________
# slide 6
class Problem:
    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        if self.state == "Arad":
            action = {"GoZerind", "GoSibiu", "GoTimisoara"}
        if self.state == "Bucharest":
            action = {"GoUrziceni", "GoPitesti", "GoGiurgiu", "GoFagaras"}
        if self.state == "Craiova":
            action = {"GoDrobeta", "GoRimnicu", "GoPitesti"}
        if self.state == "Drobeta":
            action = {"GoMehadia"}
        if self.state == "Eforie":
            action = {"GoHirsova"}
        if self.state == "Fagaras":
            action = {"GoSibiu"}
        if self.state == "Hirsova":
            action = {"GoUrziceni"}
        if self.state == "Iasi":
            action = {"GoVaslui", "GoNeamti"}
        if self.state == "Lugoj":
            action = {"GoTimisoara", "GoMehadia"}
        if self.state == "Oradea":
            action = {"GoZerind", "GoSibiu"}
        if self.state == "Pitesti":
            action = {"GoRimnicu"}
        if self.state == "Rimnicu":
            action = {"GoSibiu"}
        if self.state == "Urziceni":
            action = {"GoVaslui"}
        return action

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        if state == Arad and action == GoZerind:
            result = Zerind
        if state == Arad and action == GoSibiu:
            result = Sibiu
        if state == Arad and action == GoTimisoara:
            result = Timisoara
        if state == Bucharest and action == GoUrziceni:
            result = Urziceni
        if state == Bucharest and action == GoPitesti:
            result = Pitesti
        if state == Bucharest and action == GoGiurgiu:
            result = Giurgiu
        if state == Bucharest and action == GoFagaras:
            result = Fagaras
        if state == Craiova and action == GoDrobeta:
            result = Drobeta
        if state == Craiova and action == GoRimnicu:
            result = Rimnicu
        if state == Craiova and action == GoPitesti:
            result = Pitesti
        if state == Drobeta and action == GoMehadia:
            result = Mehadia
        if state == Eforie and action == GoHirsova:
            result = Hirsova
        if state == Fagaras and action == GoSibiu:
            result = Sibiu
        if state == Hirsova and action == GoUrziceni:
            result = Urziceni
        if state == Iasi and action == GoVaslui:
            result = Vaslui
        if state == Iasi and action == GoNeamti:
            result = Neamti
        if state == Lugoj and action == GoTimisoara:
            result = Timisoara
        if state == Lugoj and action == GoMehadia:
            result = Mehadia
        if state == Oradea and action == GoZerind:
            result = Zerind
        if state == Oradea and action == GoSibiu:
            result = Sibiu
        if state == Pitesti and action == GoRimnicu:
            result = Rimnicu
        if state == Rimnicu and action == GoSibiu:
            result = Sibiu
        if state == Urziceni and action == GoVaslui:
            result = Vaslui

        return result

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2. If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        if state1 == 'Arad' and state2 == 'Sibiu' and action == 'GoSibiu':
            return c + 1
            # c = 140
        if state1 == 'Arad' and state2 == 'Zerind' and action == 'GoZerind':
            return c + 1
            # c = 140
        if state1 == 'Arad' and action == 'GoTimisoara' and state2 == 'Timisoara':
            return c + 1
        #    c = 118
        if state1 == 'Bucharest' and action == 'GoUrziceni' and state2 == 'Urziceni':
            return c + 1
        #    c = 85
        if state1 == 'Bucharest' and action == 'GoPitesti' and state2 == 'Pitesti':
            return c + 1
        #    c = 101
        if state1 == 'Bucharest' and action == 'GoGiurgiu' and state2 == 'Giurgiu':
            return c + 1
        #    c = 90
        if state1 == 'Bucharest' and action == 'GoFagaras' and state2 == 'Fagaras':
            return c + 1
        #    c = 211
        if state1 == 'Craiova' and action == 'GoDrobeta' and state2 == 'Drobeta':
            return c + 1
        #    c = 120
        if state1 == 'Craiova' and action == 'GoRimnicu' and state2 == 'Rimnicu':
            return c + 1
        #    c = 146
        if state1 == 'Craiova' and action == 'GoPitesti' and state2 == 'Pitesti':
            return c + 1
        #    c = 138
        if state1 == 'Drobeta' and action == 'GoMehadia' and state2 == 'Mehadia':
            return c + 1
        #    c = 75
        if state1 == 'Eforie' and action == 'GoHirsova' and state2 == 'Hirsova':
            return c + 1
        #   c = 86
        if state1 == 'Fagaras' and action == 'GoSibiu' and state2 == 'Sibiu':
            return c + 1
        #   c = 99
        if state1 == 'Hirsova' and action == 'GoUrziceni' and state2 == 'Urziceni':
            return c + 1
        #   c = 98
        if state1 == 'Iasi' and action == 'GoVaslui' and state2 == 'Vaslui':
            return c + 1
        #   c = 92
        if state1 == 'Iasi' and action == 'GoNeamti' and state2 == 'Neamti':
            return c + 1
        #   c = 87
        if state1 == 'Lugoj' and action == 'GoTimisoara' and state2 == 'Timisoara':
            return c + 1
        #   c = 111
        if state1 == 'Lugoj' and action == 'GoMehadia' and state2 == 'Mehadia':
            return c + 1
        #   c = 70
        if state1 == 'Oradea' and action == 'GoZerind' and state2 == 'Zerind':
            return c + 1
        #   c = 71
        if state1 == 'Oradea' and action == 'GoSibiu' and state2 == 'Sibiu':
            return c + 1
        #  c = 151
        if state1 == 'Pitesti' and action == 'GoRimnicu' and state2 == 'Rimnicu':
            return c + 1
        # c = 97
        if state1 == 'Rimnicu' and action == 'GoSibiu' and state2 == 'Sibiu':
            return c + 1
            # c = 80
        if state1 == 'Urziceni' and action == 'GoVaslui' and state2 == 'Vaslui':
            return c + 1
        #  c = 142
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value. Hill Climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError


# ______________________________________________________________________________


class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state. Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node. Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    # We want for a queue of nodes in breadth_first_graph_search or
    # astar_search to have no duplicated states, so we treat nodes
    # with the same state as equal. [Problem: this may not be what you
    # want in other contexts.]

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        # We use the hash value of the state
        # stored in the node instead of the node
        # object itself to quickly search a node
        # with the same state in a Hash Table
        return hash(self.state)


# ______________________________________________________________________________

# ______________________________________________________________________________


class SimpleProblemSolvingAgentProgram:
    """
    [Figure 3.1]
    Abstract framework for a problem-solving agent.
    """

    def __init__(self, initial_state=None):
        """State is an abstract representation of the state
        of the world, and seq is the list of actions required
        to get to a particular state from the initial state(root)."""
        self.state = initial_state
        self.seq = []

    def __call__(self, percept):
        """[Figure 3.1] Formulate a goal and problem, then
        search for a sequence of actions to solve it."""
        self.state = self.update_state(self.state, percept)
        if not self.seq:
            goal = self.formulate_goal(self.state)
            problem = self.formulate_problem(self.state, goal)
            self.seq = self.search(problem)
            if not self.seq:
                return None
        return self.seq.pop(0)

    def update_state(self, state):
        self.state = state
        return self.state

    def formulate_goal(self, state):
        return self.state

    def formulate_problem(self, state, goal):
        problem = Problem(state, goal)
        return problem

    # ______________________________________________________________________________
    def best_first_graph_search(self, problem, f, display=False):
        """Search the nodes with the lowest f scores first.
        You specify the function f(node) that you want to minimize; for example,
        if f is a heuristic estimate to the goal, then we have greedy best
        first search; if f is node.depth then we have breadth-first search.
        There is a subtlety: the line "f = memoize(f, 'f')" means that the f
        values will be cached on the nodes as they are computed. So after doing
        a best first search you can examine the f values of the path returned."""
        f = memoize(f, 'f')
        node = Node(problem.initial)
        frontier = PriorityQueue('min', f)
        frontier.append(node)
        explored = set()
        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                if display:
                    print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
                return node
            explored.add(node.state)
            for child in node.expand(problem):
                if child.state not in explored and child not in frontier:
                    frontier.append(child)
                elif child in frontier:
                    if f(child) < frontier[child]:
                        del frontier[child]
                        frontier.append(child)
        return None

    # ______________________________________________________________________________
    # Informed (Heuristic) Search

    greedy_best_first_graph_search = best_first_graph_search

    # Greedy best-first search is accomplished by specifying f(n) = h(n).
    def astar_search(self, problem, h=None, display=False):
        """A* search is best-first graph search with f(n) = g(n)+h(n).
        You need to specify the h function when you call astar_search, or
        else in your Problem subclass."""
        h = memoize(h or problem.h, 'h')
        return best_first_graph_search(problem, lambda n: n.path_cost + h(n), display)

# ______________________________________________________________________________
