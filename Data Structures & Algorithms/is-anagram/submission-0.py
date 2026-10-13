class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = dict()
        dict2 = dict()
        if len(s) == len(t):
            for lettre in s:
                dict1[lettre] = dict1.get(lettre, 0) + 1
            for lettre in t:
                dict2[lettre] = dict2.get(lettre, 0) + 1
            if dict1 == dict2:
                return True
            else:
                return False
        else:
            return False
