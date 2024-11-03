#
#
class Solution:
    """
    The solutioln is based on the following,
    1) if hashes are not equal, the two strings will definitely not be the same
    2) if the hashes are equal, the two strings may not be the same

    What we can learn from this problem is how to hash. Python will not perform
    addtion between a str and a number. Therefore, ord(0 is needed to change a str to an int
    
    @param source: A source string
    @param target: A target string
    @return: An integer as index
    """
    def str_str2(self, source: str, target: str) -> int:
        n, m = len(source), len(target)
        if m == 0:
            return 0

        power = 1000000
        base = 1
        for i in range(m):
            base = (base * 31) % power

        src_hash, target_hash = 0, 0
        # calculate target hashes
        for i in range(m):
            target_hash = (target_hash * 31 + ord(target[i])) % power

        # calculate source hash
        for i in range(n):
            src_hash = (src_hash * 31 + ord(source[i])) % power
            #abc
            if i < m - 1:
                continue

            # abcd -> remove a
            if i >= m:
                src_hash = (src_hash - (ord(source[i - m]) * base) % power) % power
                # src_has could be negative
                if src_hash < 0:
                    src_hash = (power + src_hash) % power

            if src_hash == target_hash:
                # abc. now i = 2 points to c. m is 3, therefore, the first 
                # char is at 0, therefore, i - m + 1 = 2 -3 + 1 = 0.
                # The range is to i, therefore, we need to use i + 1
                if source[i -m + 1: i + 1] == target:
                    return i - m + 1
        return -1
