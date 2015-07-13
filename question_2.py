'''
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        num1=0
        num2=0
        count=0
        while l1:
            num1=num1+l1.val*(10**count)
            count= count +1
            l1=l1.next

        count=0
        while l2:
            num2=num2+l2.val*(10**count)
            count= count +1
            l2=l2.next

        result= num1+num2
        print 'the result', result
        print 'the len of result' ,len(str(result))

        i=0
        num_list=[]
        while i < len(str(result)):
            temp=result%(10**(i+1))
            temp=temp/(10**i)
            num_list.append(temp)
            i=i+1

        print num_list
        num_list.reverse()
        print num_list

        resultList=ListNode(num_list[0])

        for item in num_list[1:]:
            p=ListNode(item)
            p.next=resultList
            resultList=p
        return resultList


a=ListNode(1)
b=ListNode(22)

s=Solution()
print s.addTwoNumbers(a,b).val