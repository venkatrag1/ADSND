import math
from helpers import Map

def shortest_path(M, start, goal):
    """
    Find the shortest path between a start and goal node in a Map
    :param M: Map object representing interconnections between nodes
    :type M: Map
    :param start: start node
    :type start: int
    :param goal: destination node
    :type goal: int
    :return: a list of nodes in the order visited from start to goal for shortest path
    :rtype: list
    """
    a_star = AStar(M, start, goal)
    return a_star.path

class AStar(object):
    """Class representing A star path finding between start and goal nodes on a map"""
    def __init__(self, M, start, goal):
        # Input validation
        if not isinstance(M, Map):
            raise ValueError("{} is not an instance of Map".format(M))
        if not start or not goal:
            raise ValueError("start and goal nodes must be provided")
        self.M = M
        self.start = start
        self.goal = goal
        # Dictionary of current g_scores for nodes visited
        self.g_scores = {k : float('inf') for k in M.intersections}
        self.g_scores[start] = 0
        # Set of explored nodes and nodes on the frontier
        self.explored = set()
        self.frontier = set([start])
        # Dictionary of end : start pairs that can be used to reconstruct the path
        self.visited_from = dict()
        self.path = self.shortest_path()


    def distance(self, node1, node2):
        """
        Compute Euclidean distance between two nodes
        :param node1: first node
        :type node1: int
        :param node2: second node
        :type node2: int
        :return: euclidean distance
        :rtype: int
        """
        return math.sqrt(sum([(a1 - a2) ** 2 for a1, a2 in zip(self.M.intersections[node1], self.M.intersections[node2])]))

    def heuristic_cost_estimate(self, node):
        """
        An admissible heuristic cost function
        :param node: node from which cost to goal is to be calculated
        :type node: int
        :return: heuristic cost (h function)
        :rtype: int
        """
        return self.distance(node, self.goal)

    def get_tentative_gScore(self, curr_node, neighbor):
        """
        Compute what gScore would look like if this node were the path to neighbour
        :param curr_node: current node
        :type curr_node: int
        :param neighbor: node to visit
        :type neighbor: int
        :return: tentative gScore
        :rtype: int
        """
        return self.get_gScore(curr_node) + self.distance(curr_node, neighbor)

    def get_gScore(self, node):
        """
        Lookup current best gScore from dictionary
        :param node: node
        :type node: int
        :return: gScore
        :rtype: int
        """
        return self.g_scores.get(node, 0.0)

    def get_fScore(self, node):
        """
        f = g + h
        :param node: node
        :type node: int
        :return: fScore
        :rtype: int
        """
        return self.get_gScore(node) + self.heuristic_cost_estimate(node)

    def get_next_node(self):
        """
        Get minimum fScore node from the frontier
        :return: next node to visit
        :rtype: int
        """
        min_node = -1
        min_fScore = float('inf')
        for node in self.frontier:
            current_fScore = self.get_fScore(node)
            if current_fScore < min_fScore:
                min_node = node
                min_fScore = current_fScore
        return min_node

    def reconstruct_path(self, curr_node):
        """
        Retrace path from current_node to start using visited_from dictionary
        :param curr_node: current node
        :type curr_node: int
        :return: full path in reverse, from current_node to start
        :rtype: list
        """
        full_path = [curr_node]
        while curr_node in self.visited_from.keys():
            curr_node = self.visited_from[curr_node]
            full_path.append(curr_node)
        return full_path

    def get_neighbors(self, curr_node):
        return self.M.roads[curr_node]

    def record_best_path(self, curr_node, neighbor):
        """
        When we are entering or updating the gScore, also update the visited from for the new node
        :param curr_node: current node
        :type curr_node: int
        :param neighbor: node to visit
        :type neighbor: int
        :return: None
        :rtype: None
        """
        self.visited_from[neighbor] = curr_node
        self.g_scores[neighbor] = self.get_tentative_gScore(curr_node, neighbor)

    def shortest_path(self):
        """
        Find shortest path from start to goal
        :return: list of nodes in shortest route
        :rtype: list
        """
        while len(self.frontier) > 0:
            curr_node = self.get_next_node()  # Pick next minimum fScore node in frontier
            if curr_node == self.goal:  # If this is destination, done
                self.path = [x for x in reversed(self.reconstruct_path(curr_node))]
                return self.path
            else:
                self.frontier.remove(curr_node)
                self.explored.add(curr_node)  # Update lookups
            for neighbor in self.get_neighbors(curr_node):
                if neighbor in self.explored:
                    continue
                if not neighbor in self.frontier:
                    self.frontier.add(neighbor)
                if self.get_tentative_gScore(curr_node, neighbor) >= self.get_gScore(neighbor):
                    continue
                self.record_best_path(curr_node, neighbor)  # Whenever computing gScore for first time or there is a lower better gScore, update
        return []




