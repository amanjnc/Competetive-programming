class MyQueue(object):

    def __init__(self):
        S1=[]
        S2=[]
        self.S1=S1
        self.S2=S2
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.S1.append(x)
        self.S2=self.S1[::-1]

        

    def pop(self):
        """
        :rtype: int
        """
        self.S1.pop(0)
        return self.S2.pop()


        

    def peek(self):
        """
        :rtype: int
        """
        return self.S2[len(self.S2)-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.S2)==0:
            return True
        else:
            return False  
