__author__ = 'carl'
'''
Determine whether an integer is a palindrome. Do this without extra space.
Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
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