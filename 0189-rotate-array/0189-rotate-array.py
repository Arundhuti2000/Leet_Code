class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return 
        k = k % len(nums)
        i=0
        n=len(nums)
        j=n-k
        arr=[0] * n
        while j<n:
            arr[i]= nums[j]
            i+=1
            j+=1
        j=0
        while i<len(nums):
            arr[i]=nums[j]
            i+=1
            j+=1
        nums[:] = arr[:]



        