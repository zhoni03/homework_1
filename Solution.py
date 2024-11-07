class Solution(object):
    def intersection(self, nums1, nums2):
        
        l=[]
        for i in nums1:
            if i in nums2:
                if i not in l:
                    l.append(i)
        return l