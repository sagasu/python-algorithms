import unittest
import summary_ranges

class Solution(unittest.TestCase):
    def test_one(self):
        sr = summary_ranges.Solution()
        self.assertEqual(sr.summaryRanges([0,1,2,4,5,7]), ["0->2","4->5","7"])

    def test_two(self):
        sr = summary_ranges.Solution()
        self.assertEqual(sr.summaryRanges([0,2,3,4,6,8,9]), ["0","2->4","6","8->9"])


if __name__ == '__main__':
    unittest.main()