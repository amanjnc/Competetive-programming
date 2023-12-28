# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack=[]
        curr_node=head
        while curr_node is not None:
            stack.append(curr_node.val)
            curr_node=curr_node.next
        curr_node=head    
        while curr_node is not None:
            if stack.pop()!=curr_node.val:
                return False
            curr_node=curr_node.next 
        return True       


             


