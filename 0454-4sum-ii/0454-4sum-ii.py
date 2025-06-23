class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans=0
        sum_part1={}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                a_b=nums1[i]+nums2[j]
                sum_part1[a_b]=sum_part1.get(a_b, 0) + 1
        
        for k in range(len(nums3)):
            for l in range(len(nums4)):
                c_d=nums3[k]+nums4[l]
                # sum_part2[c_d]=sum_part1.get(c_d, 0) + 1
                target=-c_d
                ans+=sum_part1.get(target,0)
        return ans