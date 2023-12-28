class Solution(object):
    import copy
    def minOperations(self, s):
        
        countIfStartFromZero=0
        countIfStartFromOne=0
        se= list(s)
        sf=copy.deepcopy(se)
        for i in range(len(s)):
            j=i+1
            if i%2== 0:
                if se[i] != '0':
                    se[i] ='0'
                    countIfStartFromZero+=1    
                if sf[i] != '1':
                    sf[i] ='1'
                    countIfStartFromOne+=1       
            else:
                if se[i] != '1':
                    se[i] ='1'
                    countIfStartFromZero+=1      
                if sf[i] != '0':
                    sf[i] ='0'
                    countIfStartFromOne+=1
        return min(countIfStartFromOne,countIfStartFromZero)

    

