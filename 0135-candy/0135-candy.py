import array

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n= len(ratings)
        leftcandy=array.array('i',  [1]*len(ratings))
        rightcandy=array.array('i',  [1]*len(ratings))
        for i in range(1,n):
            if ratings[i]> ratings[i-1]:
                leftcandy[i]=leftcandy[i-1]+1
        for i in range(n - 2, -1, -1):
            if ratings[i]>ratings[i+1]:
                rightcandy[i]=rightcandy[i+1]+1
        return sum(max(leftcandy[i], rightcandy[i]) for i in range(n))


        