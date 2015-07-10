__author__ = 'carl'
'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1,-1]
        else:
            start=nums.index(target)
            i=1
            while start+i<len(nums):
                if target==nums[start+i]:
                    i=i+1
                else:
                    break
            return [start,start+i-1]


s=Solution()
print s.searchRange( [5, 7, 7, 8, 8, 10],5)