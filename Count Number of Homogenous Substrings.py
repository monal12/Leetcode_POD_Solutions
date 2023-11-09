class Solution:
    def countHomogenous(self, s: str) -> int:
        c=1
        ans=0
        for i in range(0,len(s)-1):
            if s[i]==s[i+1]:
                c+=1
            else:
                ans+=(c*(c-1))//2
                c=1
        ans+=(c*(c-1))//2
        ans+=len(s)
        return ans%(10**9+7)
