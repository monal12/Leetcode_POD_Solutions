class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        lst=[]
        for i in arr:
            b=bin(i)[2:]
            c=0
            for j in b:
                if j=='1':
                    c+=1
            lst.append([i,c])
        lst.sort(key=lambda x:(x[1],x[0]))
        ans=[]
        for i in range(len(arr)):
            ans.append(lst[i][0])
        return ans
        