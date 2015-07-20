__author__ = 'carl'
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        node_list=[]
        while head:
            node_list.append(head.val)
            head=head.next

        if len(node_list)==0:
            return []
        else:
            modified_node_list=[]
            a=len(node_list)/k
            b=len(node_list)%k
            for i in range(a):
                temp_list=[]
                for j in range(k):
                    temp_list.append(node_list[i*k+j])
                temp_list.reverse()
                modified_node_list.extend(temp_list)
            for i in range(b):
                modified_node_list.append(node_list[k*a+i])

            print modified_node_list
            return modified_node_list

s=Solution()
test=[5,4,3,2,1]
'''
head=ListNode(test[0])
for item in test[1:]:
    p=ListNode(item)
    p.next=head
    head=p
'''

head=ListNode([1])
print s.reverseKGroup(head,1)