__author__ = 'carl'
'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        first_list=[]
        while l1:
            first_list.append(l1.val)
            l1=l1.next

        second_list=[]
        while l2:
            second_list.append(l2.val)
            l2=l2.next
        first_list=first_list+second_list
        first_list.sort()
        return first_list
s=Solution()
print s.mergeTwoLists(ListNode(''),ListNode(''))
