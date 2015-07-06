__author__ = 'carl'
'''
Given a string S, find the longest palindromic substring in S.
 You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''
class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        str=list(s)
        str_reverse=list(s)
        str_reverse.reverse()

        str_len=len(str)
        max_len=0
        i=0
        print str
        print str_reverse


        return max_len
s=Solution()
print s.longestPalindrome('abbadec')