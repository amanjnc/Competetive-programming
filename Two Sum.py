class Solution(object):
    def twoSum(self, nums, target):
            self.nums=nums
            self.target=target
        
            i = 0
            j=0
        
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i!=j:
                        if nums[i]+nums[j] == target:
                            return i,j
                            j += 1

                i+=1      
   

                
