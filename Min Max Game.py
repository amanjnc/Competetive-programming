class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        print(nums)
        if len(nums)==1:  
            return nums[0]
        halflist=[]
        for i in range(len(nums)//2):
             
            num1=nums[2*i]
            num2=nums[(2*i)+1]
            if i%2==0:halflist.append(min(num1,num2))
            else:halflist.append(max(num1,num2))
             
        return self.minMaxGame(halflist)    

