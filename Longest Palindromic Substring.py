class Solution(object):
    def longestPalindrome(self, s):
      

        def innerStringEval(toLeft, toRight):
            while  toLeft >=0 and toRight<len(s) and s[toRight]==s[toLeft] :
                
                    toRight+=1
                    toLeft-=1
                
            return s[toLeft+1:toRight]
        
        result = ""
        for i in range(len(s)):
            evenPalindromeSubString=innerStringEval(i,i+1)

            oddPalindromeSubString= innerStringEval(i,i)
            largesestStringforThatindex = max(oddPalindromeSubString , evenPalindromeSubString , key=len)
            if len(largesestStringforThatindex) > len(result):
                result = largesestStringforThatindex
        return result
    


