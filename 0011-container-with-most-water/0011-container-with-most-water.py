class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_Area=0
        left = 0
        right= len(height)-1

        while left<right:
            length = min(height[left], height[right])
            width = right - left
            area = length * width
            if (area> max_Area):
                max_Area = area
            if (height[left]<height[right]):
                left+=1
            else:
                right-=1
        return max_Area

        #Brute Force Approach
        # for i in range (0, n):
        #     for j in range(i+1, n):
        #         length = min(height[i], height[j])
        #         width = i-j
        #         area = length * abs(width)
        #         if area>max_Area:
        #             max_Area= area
        # return max_Area
        