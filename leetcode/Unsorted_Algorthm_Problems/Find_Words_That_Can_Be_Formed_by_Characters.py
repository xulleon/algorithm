# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        target = set(chars)
        # Filter out unquolified word
        words = [k for k in words if set(k).issubset(target)]
        from collections import Counter
        n = len(words)
        chardict = Counter(chars)
        count = 0
        for i in range(n):
            newdict = Counter(words[i])
            found = True
            for char in newdict:
                if newdict[char] > chardict[char]:
                    # optimized to exit search
                    found = False
                    break
            if found:
                count += len(words[i])

        return count
