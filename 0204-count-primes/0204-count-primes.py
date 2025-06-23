from math import isqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        is_prime=[True]*n
        is_prime[0]=is_prime[1]=False
        ceiling=isqrt(n)
        for i in range(2,ceiling+1):
            for j in range(i*i,n,i):
                is_prime[j]=False
        return sum(is_prime)

        