class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # map = defaultdict(list)

        s1=sorted(s)
        s2=sorted(t)
        
        return s1 == s2