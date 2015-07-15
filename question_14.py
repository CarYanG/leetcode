__author__ = 'carl'
'''
Write a function to find the longest common prefix string amongst an array of strings.
'''
class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        common_pre=[]
        if len(strs)==0:
            return ''
        first_strs=list(strs[0])

        for i in range(len(first_strs)):
            flag=True
            for item in strs[1:]:
                if i>=len(list(item)):
                    flag=False
                    break
                if first_strs[i] != list(item)[i]:
                    flag=False
                    break
            print flag
            if flag:
                common_pre.append(first_strs[i])
            else:
                break

        return ''.join(common_pre)
s=Solution()
print s.longestCommonPrefix(['aca','cba'])