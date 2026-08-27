class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicti = {}
        for i in s:
            dicti[i] = dicti.get(i, 0) + 1
        for a in t:
            dicti[a] = dicti.get(a, 0) - 1
        for a in dicti:
            if dicti[a] != 0:
                return False
        return True 
        