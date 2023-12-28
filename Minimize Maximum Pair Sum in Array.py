class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)

        pairs = list()

        l = 0
        r = len(nums)-1

        result = 0
        while l < r:
            
            result = max( result, (nums[l] + nums[r]))
            l += 1
            r -= 1
            
        return result
