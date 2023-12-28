class Solution(object):
    def fourSum(self, nums, target):
        
        fourSumSet= []
        nums.sort()
        
        for i in range(len(nums)-3):
            
            if i>0 and nums[i]==nums[i-1]:
                        continue
            for j in range(i+1,len(nums)-2):
            
                if j>i+1 and  nums[j]==nums[j-1]:
                        continue
                    
                left = j + 1
                right = len(nums) - 1
                
                
                while left < right:
                    
                    singleFourSet=[nums[i],nums[j],nums[left],nums[right]]
                    
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    else:
                        right -= 1
                    if total==target and singleFourSet not in fourSumSet:
                       
                            fourSumSet.append(singleFourSet)
                    else:
                        continue
                        
                    
            
        return fourSumSet



            
