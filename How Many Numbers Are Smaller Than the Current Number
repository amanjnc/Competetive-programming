class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """        
        l=[]
        for i in range(len(nums)):
            counter=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    counter+=1
            l.append(counter)
        return  l        
    
