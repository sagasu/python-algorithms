import unittest
import longest_increasing_subsequence

class Solution(unittest.TestCase):
    def test_one(self):
        sr = longest_increasing_subsequence.Solution()
        self.assertEqual(sr.lengthOfLIS([10,9,2,5,3,7,101,18]), 4)

    # def test_two(self):
    #     sr = longest_increasing_subsequence.Solution()
    #     self.assertEqual(sr.lengthOfLIS([0,2,3,4,6,8,9]), ["0","2->4","6","8->9"])


if __name__ == '__main__':
    unittest.main()