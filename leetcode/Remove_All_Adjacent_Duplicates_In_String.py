# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
class Solution:
    def removeDuplicates(self, S: str) -> str:
        if len(S) < 2:
            return S

        start = end = len(S) - 1
        # start from end to beginning so that the removed
        # dup will not affect the indices of start and end
        while end > 0:
            while start - 1 >= 0 and S[start] == S[start - 1]:
                start -= 2
            if start == end:
                start = end = start -1
                continue

            S = S[:start+1] + S[end+1:]
            if start == len(S) -1:
                # if end is at the last position
                # 'azxxzy' or 'acbbuu'. after remove dup,
                # the start will be at index 1 and the S
                # becomes 'az' or 'ac' repectively. since
                # the index is 1, which points to the last letter.
                end = start
            else:
                # 'abbaca'. after removes first dup, it becomes
                # 'aaca', start is 0. it needs to move right 1
                # to point the second 'a' from 'aaca'
                end = start = start + 1

        return S
