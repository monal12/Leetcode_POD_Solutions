class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.res=[]
        self.recur(nestedList)

    def recur(self, nestedList):
        for i in range(len(nestedList)):
            if nestedList[i].isInteger():
                a=nestedList[i].getInteger()
                self.res.append(a)
            else:
                self.recur(nestedList[i].getList())
        
    def next(self) -> int:
        return self.res.pop(0)
        
    def hasNext(self) -> bool:
        return len(self.res)>0