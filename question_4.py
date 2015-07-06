__author__ = 'carl'
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
 Find the median of the two sorted arrays.
 The overall run time complexity should be O(log (m+n)).
'''
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        for item in nums2:
                nums1.append(item)
        nums1=sorted(nums1)
        if len(nums1)%2==0:

            return (nums1[len(nums1)/2-1]+nums1[len(nums1)/2])/2.0
        else:
            return nums1[len(nums1)/2]/1.0

s=Solution()
print s.findMedianSortedArrays([1,1],[1,2])




