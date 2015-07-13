__author__ = 'carl'
'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        str_list=s.strip().split(" ")
        if '' in str_list and len(str_list)==0:
            return 0
        else:
            return len(list(str_list[len(str_list)-1]))

s=Solution()
print s.lengthOfLastWord("      ")
