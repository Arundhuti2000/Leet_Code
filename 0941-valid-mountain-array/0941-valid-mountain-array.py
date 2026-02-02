class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        index=0
        n= len(arr)
        if n<3:
            return False
        for i in range(n-1):
            if arr[i+1]<=arr[i]:
                index= i
                break
        else:
            return False
        if index==0 or index==n-1:
            return False
        for j in range(index, n-1):
            if arr[j+1]>=arr[j]:
                return False
        return True

    
        
