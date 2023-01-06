class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s2=[]
        for i in range(len(s)):
            if s[i]=="(":
                s2.append(s[i])
            elif s[i]=="{":
                s2.append(s[i])
            elif s[i]=="[":
                s2.append(s[i])
            elif s[i]==")":
                if len(s2)==0:
                    return False
                elif  s2.pop()=="(":
                    continue
                else:
                    return False
            elif  s[i]=="}":
                if len(s2)==0:
                    return False
                elif  s2.pop()=="{":
                    continue
                else:
                    return False
            elif  s[i]=="]":
                if len(s2)==0:
                    return False

                elif s2.pop()=="[":
                    continue
                else:
                    return False

        if len(s2)==0:
                return True
        else:
                return False                  
            
