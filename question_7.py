__author__ = 'carl'
'''
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
'''
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        str_list=list(str(x))
        if str_list[0]=='-':
            temp=str_list[1:len(str_list)]
            temp.reverse()
            temp.insert(0,'-')
            if int(''.join(temp))<-2147483648:
                return 0
            else:
                return int(''.join(temp))
        else:
            str_list.reverse()
            if int(''.join(str_list))>2147483647:
                return 0
            else:
                return int(''.join(str_list))



s=Solution()
print s.reverse(1534236469)