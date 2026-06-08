class Solution:
    def searchRange(self, n: List[int], key: int) -> List[int]:
        low=0
        high=len(n)-1
        found1=-1

        while(low<=high):
            mid=(low+high)//2
            if n[mid]==key:
                found1=mid
                high=mid-1
            elif n[mid]<key:
                low=mid+1
            else:
                high=mid-1
        if found1==-1:
            return [-1,-1]

        low=0
        high=len(n)-1
        found2=-1
        while(low<=high):
            mid=(low+high)//2
            if n[mid]==key:
                found2=mid
                low=mid+1
            elif n[mid]<key:
                low=mid+1
            else:
                high=mid-1
        return [found1,found2]

        
