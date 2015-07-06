__author__ = 'carl'
'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
 n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
 Find two lines, which together with x-axis forms a container, such that the container contains the most water.
'''
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        max_container=0.0
        point_len=len(height)
        for i in range(point_len):
            for j in range(i+1,point_len):
                c_height=height[i] if height[i]<=height[j] else height[j]
                if max_container/(j-i)>=c_height:
                    pass
                else:
                    temp_container=(j-i)*float(c_height)
                    if temp_container>max_container:
                        max_container=temp_container
        return max_container

s=Solution()
print s.maxArea([3,5,6])
