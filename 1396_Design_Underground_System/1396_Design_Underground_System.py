"""
Question:
An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel 
from one station to another.

Implement the UndergroundSystem class:

void checkIn(int id, string stationName, int t)
A customer with a card ID equal to id, checks in at the station stationName at time t.
A customer can only be checked into one place at a time.
void checkOut(int id, string stationName, int t)
A customer with a card ID equal to id, checks out from the station stationName at time t.
double getAverageTime(string startStation, string endStation)
Returns the average time it takes to travel from startStation to endStation.
The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by 
a check out from endStation.
The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen 
in chronological order.

Soln:
use dict to store info - time, count and cur id data if any
"""
class UndergroundSystem(object):

    def __init__(self):
        from collections import defaultdict
        self.pair = defaultdict(int)
        self.freq = defaultdict(int)
        self.data = defaultdict()

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.data[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        station1, t1 = self.data[id]
        self.pair[(station1, stationName)] += t - t1
        self.freq[(station1, stationName)] +=1
        del self.data[id]

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        return float(self.pair[(startStation, endStation)])/self.freq[(startStation, endStation)]