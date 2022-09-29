# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        dp = {'X':'O', 'O':'X'}
        matrix = [[None] * 3 for _ in range(3)]
        char = 'X'
        for x, y in moves:
            matrix[x][y] = char
            char = dp[char]

        print(matrix)
        return self.checkMatrix(matrix)

    def checkMatrix(self, matrix):
        dp = {'X': 'A', 'O': 'B'}
        # check each row
        for char in ['X', 'O']:
            lrcross = []

            columcount = 0
            for i in range(3):
                lrcross.append(matrix[i][i])
                if matrix[i].count(char) == 3:
                    return dp[char]
            if lrcross.count(char) == 3:
                return dp[char]

            for j in range(3):
                rlcross = []
                for i in range(3):
                    rlcross.append(matrix[i][j])
                if rlcross.count(char) == 3:
                    return dp[char]

            if [matrix[0][2], matrix[1][1], matrix[2][0]].count(char) == 3:
                return dp[char]

        return 'Pending' if self.totalfilled(matrix) < 9 else 'Draw'


    def totalfilled(self, matrix):
        allstr = ''
        for i in range(3):
            allstr += ''.join([k for k in matrix[i] if k is not None])
        return len(allstr)
