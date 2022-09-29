# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        dp = {0:0}
        inventory.sort(reverse=True)
        num_colors = len(inventory)
        start, end = 0, num_colors
        index, layers, leftover = self.findPointer(inventory, orders, 0, num_colors, dp)
        return self.calculate_cost(inventory, index, layers, leftover)

    def findPointer(self, invtry, orders, start, end, dp):
        n = len(invtry)
        while start + 1 < end:
            # Binary search if a color(index) can be found between
            # the first color and last color
            mid = start + (end - start) // 2
            if mid in dp:
                balls = dp[mid]
            else:
                balls = sum([invtry[i] - invtry[mid] for i in range(mid)])
                dp[mid] = balls

            if balls > orders:
                # use less colors.remember that the colors have
                # been sorted in descending order
                end = mid
            elif balls <= orders <= balls + mid + 1 or mid == n - 1:
                # check if mid reaches the end of the color.
                # then need 3rd variable for how mancy deep to got the layers.
                #found it
                leftover = orders - balls
                layers = 0
                if mid == n - 1:
                    layers = leftover // n
                    leftover %= n

                return mid, layers, leftover
            else:
                # balls < orders. use more colors
                start = mid

            return self.findPointer(invtry, orders, start, end, dp)
        # When color can not be found by normal binary search of the above while loop
        # Below covers 3 scenarios:
        # 1) inventory has only one color means len(inventory) == 1
        # 2) the first color meets all requirements for order.
        #.   rest colors are not needed at all
        # 3)  get into this point where "end - start == 1"
        #     dp[end] > orders but dp[start] < orders. Since start
        #.    is not zero, then color from 0 to start will be used.
        leftover = orders - dp[start]
        layers = leftover // (start + 1)
        leftover = 0 if start == 0 else leftover % (start + 1)
        return start, layers, leftover

    def calculate_cost(self, invtry, index, layers, leftover):
        if index == 0:
            return ((2 * invtry[index] - layers + 1 ) * layers // 2) % (10**9 + 7)

        cost = 0
        # invtry[index] was exclusive
        base = invtry[index]
        for i in range(index):
            top = invtry[i]
            cost = (cost + (top + base + 1) * (top - base) //2) % (10**9 + 7)
        if layers > 0:
            cost = (cost + (index + 1) * (2 * invtry[index] - layers + 1) * layers // 2) % (10**9 + 7)

        if leftover > 0:
            cost += (invtry[index] - layers) * leftover

        return cost % (10**9 + 7)

