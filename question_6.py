#-*-coding:utf-8-*-
__author__ = 'carl'
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
 (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
'''
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        str_list=list(s)
        str_lists=[[]for i in range (numRows)]
        str_len=len(str_list)
        if numRows==1:
            return s
        else:
            for i in range(str_len):
                if i % (numRows+numRows-2)>=numRows:
                    str_lists[numRows-1-(i%(numRows+numRows-2))%(numRows-1)].append(str_list[i])
                else:
                    str_lists[i%(numRows+numRows-2)].append(str_list[i])
            for i in range(1,numRows):
                str_lists[0].extend(str_lists[i])

            return ''.join(str_lists[0])

s=Solution()
print s.convert('A',1)

'''
思路：
0        8
1     7  9
2   6    10
3 5      11
4        12
先不管中间的单个的数字，每一行都是除以8得到相同的余数，这个8就是行数的2倍减去2，即numRows+numRows-2
然后再看中间单个的数字，他们对8的余数都大于numRow，可以找到他们与所在行之间的关系，，
总之就是找规律求解
'''
