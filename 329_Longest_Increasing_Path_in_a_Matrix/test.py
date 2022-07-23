from LongestPathMatrix import LPM


import unittest
class TestCalendar(unittest.TestCase):
    def test_1(self):
        test1 = LPM()
        matrix = [[9,9,4],[6,6,8],[2,1,1]]
        ans = test1.longestIncreasingPath(matrix)
        print(ans)

if __name__ == '__main__':
    unittest.main()

