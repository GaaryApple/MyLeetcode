"""
Question:
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.
Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Soln:
target: 1<<n - 1
bfs search until mask == target and return time
mask[i]: path of starting point 0:n-1
seen: aovid repetition 
"""
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        from collections import deque
        n = len(graph)
        mask = [1<<i for i in range(n)]
        target = (1<<n) - 1
        queue = deque([i, mask[i]] for i in range(n))
        seen = [{mask[i]} for i in range(n)]
        step = 0
        
        while queue:
            for _ in range(len(queue)):
                node, mask = queue.popleft()
                if mask == target:
                    return step
                for nei in graph[node]:
                    newmask = mask|(1<<nei)
                    if newmask not in seen[nei]:
                        queue.append((nei, newmask))
                        seen[nei].add(newmask)
            step +=1
        return step

