__author__ = 'carl'
'''
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        #if len(nums)==1:
            #return nums[0]
        single_num=nums[0]
        for i in range(3):
            for item in nums[1:]:
                single_num=single_num^item
        return single_num

s=Solution()
print s.singleNumber([1,2,3,4,1,2,3,4,1,2,3,4,5])

