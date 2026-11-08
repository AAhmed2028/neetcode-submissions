class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS=list(s)
        listT=list(t)
        if sorted(listT)==sorted(listS):
            return True
        return False
        