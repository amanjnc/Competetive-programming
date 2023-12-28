class Solution(object):
    def reverse(self, x):   

        c=1
        reversed=0
        if x<0:
            x *= -1
            c=-1
        while x>0:
            remainder = x%10
            x= x//10
            reversed = reversed*10 + remainder
        if c == -1:
            reversed*=-1
        if reversed >= 2**31 - 1:
            return 0  
        if -2**31 >= reversed  :
            return 0
    
        return reversed
    
