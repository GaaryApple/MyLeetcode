from mycalendar import MyCalendarThree

import unittest
class TestCalendar(unittest.TestCase):
    def test_1(self):
        obj = MyCalendarThree()
        ans1 = obj.book(10, 20)
        print(ans1)
        ans2 = obj.book(15, 25)
        print(ans2)
        ans3 = obj.book(20, 30)
        print(ans3)


if __name__ == '__main__':
    unittest.main()



    