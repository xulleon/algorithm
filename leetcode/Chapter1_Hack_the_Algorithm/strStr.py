# https://www.lintcode.com/problem/13/
# 65 ms time cost· 5.04 MB memory cost· Your submission beats 62.60 % Submissions
def str_str(self, source: str, target: str) -> int:
    # Write your code here
    n, m = len(source), len(target)
    if n < m:
        return -1

    if m == 0:
        return 0

    for i in range(n):
        if i + m - 1 > n:
            break

        if source[i] == target[0] and source[i: i + m] == target:
            return i
    return -1
