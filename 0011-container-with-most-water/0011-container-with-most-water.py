class Solution:
    def maxArea(self, height: List[int]) -> int: 
        left = 0 
        right = len(height)-1
        max_vol = float('-inf')
        while (left < right):
            h1 = height[left]
            h2 = height[right]

            vol = min(h1,  h2) * (right - left)
            max_vol = max(max_vol , vol)

            if h1 <= h2:
                left+=1
            else:
                right-=1
        return max_vol 
    