from collections import defaultdict
from typing import List

class ThroneInheritance:
    def _init__(self, kingName: str): 
        self.children = defaultdict(list) 
        self.death =set()
        self.kingName = kingName
    def birth(self, parentName: str, childName: str) -> None: 
        self.children[parentName].append(childName)
    def death(self, name: str) -> None: 
        self.death.add(name)
    def getInheritanceOrder(self) -> List[str]: 
        ans = []
        def dfs(person):
            if person not in self.death:
                ans.append(person)
            for child in self.children[person]: 
                dfs(child)

        dfs(self.kingName)

        return ans
