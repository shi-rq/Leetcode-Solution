'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
is able to trap after raining.

       +
   ++++++++
 +++++++++++

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water
(blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height : return 0
        full = [0 for n in range(len(height))]
        maxheight = max(height)
        for climb in range(1, maxheight+1):
            if climb in height:
                for n in range(len(height)):
                    if height[n] >= climb:
                        lh = n
                        break
                for n in range(len(height))[::-1]:
                    if height[n] >= climb:
                        rh = n
                        break
                for n in range(lh, rh+1):
                    full[n] = climb
        rain = 0
        for n in range(len(height)):
            rain += (full[n] - height[n])
        return rain