__author__ = 'carl'
'''
Given a string, find the length of the longest substring without repeating characters. For example,
the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
 For "bbbbb" the longest substring is "b", with the length of 1.
'''
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        str=list(s)
        temp=set()
        max_len_sub=0
        i=0
        for item in str[i:]:
            len_sub=0
            if len(temp)!=len(temp.append(item)):
                len_sub=len_sub+1
            elif len_sub==len(str):
                max_len_sub=len(str)
                break
            elif len(temp)==len(temp.append(item)):
                max_len_sub=len_sub
                i=i+1








