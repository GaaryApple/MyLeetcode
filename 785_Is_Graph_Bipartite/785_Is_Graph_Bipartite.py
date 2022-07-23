"""
Question: 
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that 
node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:
There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.
Return true if and only if it is bipartite.


Soln:
for each node (edge), dfs search if its connected nodes can be splited into two parents, if yes continue if not return False

"""

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        seen = {}
        for node in range(n):
            if node not in seen:
                seen[node] = 0
                if not self.dfs(node, graph, seen):
                    return False
        return True

    def dfs(self, node, graph, seen):
        for nei in graph[node]:
            if nei in seen:
                if seen[node] == seen[nei]:
                    return False
            else:
                seen[nei] = 1 - seen[node]
                if not self.dfs(nei, graph, seen):
                    return False
        return True