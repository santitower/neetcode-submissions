class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # can sort all of the strings, and if they are they same then it can be considered that they are the same 
        s = sorted(s)
        t= sorted(t)
        if s == t: return True 
        else: return False

        