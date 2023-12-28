class Solution(object):
    def threeSumClosest(self, nums, target):
        closestDistance = float('inf')
        nums.sort()
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if abs(total - target) < abs(closestDistance - target):
                    closestDistance = total
                
                if total < target:
                    left += 1
                else:
                    right -= 1
        
        return closestDistance


