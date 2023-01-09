class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(len(nums)):
            if nums[j] == 0:
                nums.pop(j)
                nums.insert(0, 0)
                j+=1
                 
            elif nums[j] == 2:
                nums.pop(j)
                nums.append(2)
            
            else:
                
                j+=1  
        return nums                  
    
