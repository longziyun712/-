class Solution:
    def singleNumber(self, nums):
        n=0
        for i in nums:
            n^=i
        return n 