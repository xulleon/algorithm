# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        notedict, magdict = Counter(ransomNote), Counter(magazine)
        for char in notedict:
            if char not in magdict:
                return False

            if notedict[char] > magdict[char]:
                return False

        return True

