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
        str=list(s) # conver string to a list
        max_len_sub=1 #set the lenght of longest substring
        len_string=len(str)

        for i in range (len_string):
            if len_string-i>=max_len_sub:
                temp=set(str[i:i+max_len_sub])
                for item in str[i:]:
                    curr_len=len(temp)
                    if curr_len<max_len_sub:
                        break
                    if len(temp)>=len_string-str.index(item):
                        return len(temp)
                    temp.add(str[str.index(item)+max_len_sub])
                    if curr_len==len(temp):
                        max_len_sub=curr_len
                        break

        return max_len_sub

s=Solution()
print s.lengthOfLongestSubstring('avs')





