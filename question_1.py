'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
 where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        for item in num:
            if target-item in num:
                if item+item!=target:
                    return (num.index(item)+1,num.index(target-item)+1)
                elif item+item==target:
                    temp=num[num.index(item)+1:]
                    if  target-item in temp:
                        return (num.index(item)+1,num.index(item)+temp.index(target-item)+2)


num=[-1,-2,-2,-5]
tar=-4
s=Solution()
a=s.twoSum(num,tar)
print a