__author__ = 'carl'
'''
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if val not in nums:
            return len(nums)
        else:
            while val in nums:
                del nums[nums.index(val)]
            return len(nums)

s=Solution()
print s.removeElement([1,2,1,1,2,3,4,5],2)
