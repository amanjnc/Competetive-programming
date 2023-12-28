class Solution(object):
    def minDeletionSize(self,strs):
            deleted_col = 0        
            y = len(strs)
            z = len(strs[0])
            for j in range(z):
                for i in range(y-1):
                    if strs[i][j] > strs[i+1][j]:
                        deleted_col += 1
                        break
                    else:
                        continue
            return(deleted_col)        



                
                
                
                
            
