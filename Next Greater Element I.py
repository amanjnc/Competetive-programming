class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
       
        m = {}
        stk = []
        for v in nums2:
            while stk and stk[-1] < v:
                m[stk.pop()] = v
            stk.append(v)
        return [m.get(v, -1) for v in nums1]
