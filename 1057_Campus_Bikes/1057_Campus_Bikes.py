"""
Question:
On a campus represented on the X-Y plane, there are n workers and m bikes, with n <= m.
You are given an array workers of length n where workers[i] = [xi, yi] is the position of the ith worker. You are also given an array bikes of length m 
where bikes[j] = [xj, yj] is the position of the jth bike. All the given positions are unique.
Assign a bike to each worker. Among the available bikes and workers, we choose the (workeri, bikej) pair with the shortest Manhattan distance between each other 
and assign the bike to that worker.
If there are multiple (workeri, bikej) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index. If there are multiple ways to do that, 
we choose the pair with the smallest bike index. Repeat this process until there are no available workers.
Return an array answer of length n, where answer[i] is the index (0-indexed) of the bike that the ith worker is assigned to.
The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

soln:
build dict with distances per workers and sort reversely for each dict[worker_id]
priority queue, pop smallest (d, worker_id, bike_id), if bike_id not used, then add to ans; if not pop next samllest from dict[worker_id] and push into heap   
go to next candiate

"""
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        import heapq
        from collections import defaultdict
        dist = defaultdict(list)
        n, m = len(workers), len(bikes)
        for i in range(n):
            for j in range(m):
                d = abs(workers[i][0] -  bikes[j][0]) + abs(workers[i][1] -  bikes[j][1])
                dist[i].append((d, i, j))
            dist[i].sort(reverse = True)
        h = [dist[i].pop() for i in range(n)]
        heapq.heapify(h)
        ans = [None] * n
        seen = [0] * m
        while h:
            _, worker_id, bike_id = heapq.heappop(h)
            if seen[bike_id] == 0:
                seen[bike_id] = 1
                ans[worker_id] = bike_id
            else:
                heapq.heappush(h, (dist[worker_id].pop()))

        return ans