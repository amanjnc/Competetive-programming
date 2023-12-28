class Solution(object):
    def maxScore(self, s):
       
        le = len(s) 
        stackleft = [s[0]]
        stackright = list(s[1:le])
        countleft = 0
        countright = 0
        sumlist = []

        while len(stackright) > 0:
            countleft = stackleft.count("0")
            countright = stackright.count("1")
            total_sum = countleft + countright
            stackleft.append(stackright[0])
            stackright = stackright[1:]
            sumlist.append(total_sum)

        return max(sumlist)
