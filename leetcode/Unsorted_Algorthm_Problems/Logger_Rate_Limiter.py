# https://leetcode.com/problems/logger-rate-limiter/
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.logger = {}


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.logger or timestamp >= self.logger[message] + 10:
            self.logger[message] = timestamp
            return True
        else:
            return False
