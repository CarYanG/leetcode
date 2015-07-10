__author__ = 'carl'
'''
Determine whether an integer is a palindrome. Do this without extra space.
'''
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x <0:
            return False
        x_copy=x
        a=x%10
        reverse_x=0
        while True:
            reverse_x=reverse_x*10+a
            x=x/10
            if x==0:
                break
            a=x%10
        if reverse_x==x_copy:
            return True
        else:
            return False

s=Solution()
print s.isPalindrome(-2147483648)