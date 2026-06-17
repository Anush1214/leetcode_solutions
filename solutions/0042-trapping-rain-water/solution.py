class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left=0
        right=len(height)-1
        maxl,maxr=0,0
        maxw=0

        while left<right:
            if height[left]<height[right]:
                if height[left]>=maxl:
                    maxl=height[left]
                else:
                    maxw+=maxl-height[left]
                left+=1
            else:
                if height[right]>=maxr:
                    maxr=height[right]
                else:
                    maxw+=maxr-height[right]
                right-=1
        return maxw
