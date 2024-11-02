# https://leetcode.com/problems/longest-palindromic-subsequence/
# Runtime: 964 ms, faster than 47.57% of Python3 online submissions for Longest Palindromic Subsequence.
# Memory Usage: 33.1 MB, less than 69.16% of Python3 online submissions for Longest Palindromic Subsequence.
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        
        dp = [[1] * n for i in range(n)]
        max_len = 1
        # Step1: initialize diagnal for length as 1
        for i in range(n):
            dp[i][i] = 1
        
        # Step2: initialize cell with length as 2
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 2
                max_len = 2
        
        start1, end1 = 0, 0
        # Step 3: for a string with n chars, fro ith to 
        # jth substring, the subsequence is max(dp[i-1][j], dp[i][j-1])
        for dist in range(3, n + 1):
            for start in range(n):
                end = start + dist - 1
                if end >= n:
                    break
                
                if s[start] == s[end]:
                    dp[start][end] = dp[start + 1][end - 1] + 2
                    start1, end1 = start, end
                    if dp[start][end] > max_len:
                        max_len = dp[start][end]
                else:
                    dp[start][end] = max(dp[start][end-1], dp[start+1][end])
                
        return max_len
