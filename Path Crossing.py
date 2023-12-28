class Solution(object):
    def isPathCrossing(self, path):
        visitedPoints = [(0,0)]

        for i in path :
            lastVisted = list(visitedPoints)[-1]
            newlyVisted = (lastVisted[0], lastVisted[1] + 1)

            if i== 'N':
                newlyVisited = (lastVisted[0], lastVisted[1] + 1)
                
            elif i == 'S':
                newlyVisited = (lastVisted[0], lastVisted[1]-1)
                
                
            elif i == 'E':
                newlyVisited = (lastVisted[0]+1, lastVisted[1] )
                
            elif i == 'W':
                newlyVisited = (lastVisted[0]-1, lastVisted[1] )
                
            if newlyVisited in visitedPoints:
                return True
            else:    
                visitedPoints.append(newlyVisited)
        return False
