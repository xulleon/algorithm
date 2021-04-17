# https://leetcode.com/problems/design-tic-tac-toe/
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [[0] * n for _ in range(n)]


    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = player
        return self.check(row, col, player)

    def check(self, row, col, player):
        count = 0
        n = len(self.board)
        #horizontal
        for i in range(n):
            if self.board[row][i] == player:
                count += 1

        if count == n:
            return player

        count = 0
        for i in range(n):
            if self.board[i][col] == player:
                count += 1
        if count == n:
            return player

        # left to right cross
        if row - col == 0:
            count = 0
            for i in range(n):
                if self.board[i][i] == player:
                    count += 1
            if count == n:
                return player

        # righ to left cross.
        if row + col == n - 1:
            count, i, j = 0, 0, n - 1
            for k in range(n):
                if self.board[i][j] == player:
                    count += 1
                i, j = i + 1, j - 1
            if count == n:
                return player

        return 0

