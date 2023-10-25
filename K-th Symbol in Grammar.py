class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def recur(n,k):
            if n==1 and k==1:
                return 0
            mid=(2**(n-1))//2
            if k<=mid:
                return recur(n-1,k)
            else:
                return 1-recur(n-1,k-mid)
        return recur(n,k)

