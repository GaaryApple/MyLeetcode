"""
Question:

A concert hall has n rows numbered from 0 to n - 1, each with m seats, numbered from 0 to m - 1. You need to design a ticketing system that can allocate seats in the following cases:

    -If a group of k spectators can sit together in a row.
    -If every member of a group of k spectators can get a seat. They may or may not sit together.
Note that the spectators are very picky. Hence:

    -They will book seats only if each member of their group can get a seat with row number less than or equal to maxRow. maxRow can vary from group to group.
    -In case there are multiple rows to choose from, the row with the smallest number is chosen. If there are multiple seats to choose in the same row, the seat with the smallest 
    number is chosen.

Implement the BookMyShow class:
   -BookMyShow(int n, int m) Initializes the object with n as number of rows and m as number of seats per row.
   -int[] gather(int k, int maxRow) Returns an array of length 2 denoting the row and seat number (respectively) of the first seat being allocated to the k members of the group, 
    who must sit together. In other words, it returns the smallest possible r and c such that all [c, c + k - 1] seats are valid and empty in row r, and r <= maxRow. 
    Returns [] in case it is not possible to allocate seats to the group.
   -boolean scatter(int k, int maxRow) Returns true if all k members of the group can be allocated seats in rows 0 to maxRow, who may or may not sit together. If the seats can be 
    allocated, it allocates k seats to the group with the smallest row numbers, and the smallest possible seat numbers in each row. Otherwise, returns false.

"""

class Node():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
        self.mx = 0
        self.tot = 0

class Segtree():
    def __init__(self, start, end, val):
        def createTree(lo, hi):
            if lo > hi:
                return None
            if lo == hi:
                node = Node(lo, hi)
                node.mx = val
                node.tot = val
                return node
            node = Node(lo, hi)
            mid = (lo+hi)//2
            node.left = createTree(lo, mid)
            node.right = createTree(mid+1, hi)
            node.tot = node.left.tot + node.right.tot
            node.mx = max(node.left.mx, node.right.mx)
            return node
        self.root = createTree(start, end)

    def update(self, idx, val):
        def updateTree(node):
            if node.start == node.end == idx:
                node.tot -= val
                node.mx -= val
                return 
            mid = (node.start + node.end)//2
            if idx <= mid:
                updateTree(node.left)
            else:
                updateTree(node.right)
            node.tot = node.left.tot + node.right.tot
            node.mx = max(node.left.mx, node.right.mx)
            return 
        updateTree(self.root)

    def queryMax(self, k, maxRow, seats):
        def helpmax(node):
            if node.start == node.end:
                if node.end > maxRow or node.tot < k:
                    return []
                if node.end <= maxRow and node.tot >= k:
                    return [node.end, seats - node.tot]
            if node.left.mx >= k:
                return helpmax(node.left)
            return helpmax(node.right)
        return helpmax(self.root)

    def querySum(self, maxRow):
        def helpSum(node, left, right):
            if left > node.end or right < node.start:
                return 0
            if left == node.start and right == node.end:
                return node.tot
            mid = (node.start + node.end)//2
            if right <= mid:
                return helpSum(node.left, left, right)
            elif left > mid:
                return helpSum(node.right, left, right)
            else:
                return helpSum(node.left, left, mid) + helpSum(node.right, mid+1, right)
        return helpSum(self.root, 0, maxRow)


class BookMyShow(object):

    def __init__(self, n, m):
        self.st = Segtree(0, n-1, m)
        self.seats = [m] * n
        self.m = m
        self.row = 0

    def gather(self, k, maxRow):
        res = self.st.queryMax(k, maxRow, self.m)
        if res:
            r = res[0]
            self.st.update(r, k)
            self.seats[r] -=k
        return res

    def scatter(self, k, maxRow):
        if self.st.querySum(maxRow) < k:
            return False
        tot = 0
        r = self.row
        while tot < k:
            prev = tot
            tot += self.seats[r]
            if tot < k:
                self.st.update(r, self.seats[r])
                self.seats[r] = 0
                self.row = r
                r +=1
            else:
                self.st.update(r, k -prev)
                self.seats[r] -= k -prev
        return True   
