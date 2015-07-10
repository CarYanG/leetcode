#-*- coding:utf-8 -*-
__author__ = 'carl'
'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if target in nums:
            return  nums.index(target)
        else:
            i=0
            while i<len(nums):
                if nums[i]>target:
                    return i
                else:
                    i=i+1

            return i

s=Solution()
print s.searchInsert([1,2,5,6],4)