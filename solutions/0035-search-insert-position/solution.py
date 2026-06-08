class Solution:
    def searchInsert(self, n: List[int], key: int) -> int:
        low=0
        high=len(n)-1
        found=False
        mid=0
        if key<n[0]:
            return 0
        while(low<=high):
            mid=(low+high)//2
            if n[mid]==key:
                found=True
                return mid
                break
            elif n[mid]<key:
                low=mid+1
            else:
                high=mid-1

        if not found:
            return low
