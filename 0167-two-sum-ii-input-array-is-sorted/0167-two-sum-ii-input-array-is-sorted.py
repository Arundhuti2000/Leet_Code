class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            compliment = target - numbers[i]
            if (compliment in seen):
                return seen.get(compliment)+1, i+1
            else: 
                seen[numbers[i]] = i