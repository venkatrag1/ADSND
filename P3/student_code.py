import math
from helpers import Map
import heapq

def shortest_path(M, start, goal):
    route_planner = RoutePlanner(M, start, goal)
    return route_planner.path

class RoutePlanner(object):
    def __init__(self, M, start, goal):
        if not isinstance(M, Map):
            raise ValueError("{} is not an instance of Map".format(M))
        if not start or not goal:
            raise ValueError("start and goal nodes must be provided")
        self.M = M
        self.start = start
        self.goal = goal
        self.g_scores = {k : float('inf') for k in M.intersections}
        self.g_scores[start] = 0
        self.explored = set()
        self.frontier = set([start])
        self.visited_from = dict()
        self.path = self.shortest_path()


    def distance(self, node1, node2):
        return math.sqrt(sum([(a1 - a2) ** 2 for a1, a2 in zip(self.M.intersections[node1], self.M.intersections[node2])]))

    def heuristic_cost_estimate(self, node):
        return self.distance(node, self.goal)

    def get_tentative_gScore(self, curr_node, neighbor):
        return self.get_gScore(curr_node) + self.distance(curr_node, neighbor)

    def get_gScore(self, node):
        return self.g_scores.get(node, 0.0)

    def get_fScore(self, node):
        return self.get_gScore(node) + self.heuristic_cost_estimate(node)

    def get_next_node(self):
        min_node = -1
        min_fScore = float('inf')
        for node in self.frontier:
            current_fScore = self.get_fScore(node)
            if current_fScore < min_fScore:
                min_node = node
                min_fScore = current_fScore
        return min_node

    def reconstruct_path(self, curr_node):
        full_path = [curr_node]
        while curr_node in self.visited_from.keys():
            curr_node = self.visited_from[curr_node]
            full_path.append(curr_node)
        return full_path

    def get_neighbors(self, curr_node):
        return self.M.roads[curr_node]

    def record_best_path(self, curr_node, neighbor):
        self.visited_from[neighbor] = curr_node
        self.g_scores[neighbor] = self.get_tentative_gScore(curr_node, neighbor)

    def shortest_path(self):
        while len(self.frontier) > 0:
            curr_node = self.get_next_node()
            if curr_node == self.goal:
                self.path = [x for x in reversed(self.reconstruct_path(curr_node))]
                return self.path
            else:
                self.frontier.remove(curr_node)
                self.explored.add(curr_node)
            for neighbor in self.get_neighbors(curr_node):
                if neighbor in self.explored:
                    continue
                if not neighbor in self.frontier:
                    self.frontier.add(neighbor)
                if self.get_tentative_gScore(curr_node, neighbor) >= self.get_gScore(neighbor):
                    continue
                self.record_best_path(curr_node, neighbor)
        return None




