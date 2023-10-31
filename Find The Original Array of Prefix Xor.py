class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        lst=[]
        for i in range(len(pref)-1,0,-1):
            lst.append(pref[i]^pref[i-1])
        lst.append(pref[0])
        return lst[::-1]