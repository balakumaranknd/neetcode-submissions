class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
            
        dct1, dct2 = {}, {}

        for st in s:
            if st not in dct1.keys():
                dct1[st] = 1
            else:
                dct1[st] += 1
        
        for st in t:
            if st not in dct2.keys():
                dct2[st] = 1
            else:
                dct2[st] += 1

        return dct1 == dct2


        