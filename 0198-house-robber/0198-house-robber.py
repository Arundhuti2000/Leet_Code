class Solution:
    def robhouse(self,houses, i,dp):
            if dp[i] is not None:
                return dp[i]
            if i <0:
                return 0
            if i==0:
                return houses[0]
            if i==1:
                return max(houses[0],houses[1])
            ith_houose_stolen=houses[i] + self.robhouse(houses,i-2,dp)
            ith_houose_not_stolen=self.robhouse(houses,i-1,dp)
            dp[i]=max(ith_houose_stolen,ith_houose_not_stolen)
            return dp[i]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [None] * n
        return self.robhouse(nums, n-1,dp)

        