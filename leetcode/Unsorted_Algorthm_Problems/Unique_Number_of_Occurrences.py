# https://leetcode.com/problems/unique-number-of-occurrences/
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        # if occurance is unique, then the number of
        # occurance must be equal to the number of unique integers
        return len(set(Counter(arr).values())) == len(set(arr))
