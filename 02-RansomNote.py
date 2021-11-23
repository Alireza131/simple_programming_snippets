from collections import defaultdict

class Solution(object):
    def CanSpell(self,magazine, note):
        letters=defaultdict(int) #initialize a defaultdict
        for c in magazine:
            letters[c]=1
        for c in note:
            if letters[c]<=0:
                return False
            letters[c] -= 1
        return True

print(Solution().CanSpell(['a','b','c','d','e','f','g'],'back'))
print(Solution().CanSpell(['a','b','c','d','e','f','g'],'bed'))