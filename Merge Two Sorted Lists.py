# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # create the new linkedlist
        mergedhead =ListNode(10000)
        current=mergedhead
        while list2 and list1:
             if list2.val < list1.val:
                current.next = list2
                list2=list2.next
             else:
                current.next = list1
                list1=list1.next
             current=current.next   
        if list2:
            current.next= list2
        else:
            current.next=list1
        mergedhead=mergedhead.next
        return mergedhead
