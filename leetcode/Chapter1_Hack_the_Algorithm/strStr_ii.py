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
        # write your code here
        n, m = len(source), len(target)
        if m == 0:
            return 0

        base = 1000000
        power = 1
        for i in range(m):
            power = (power * 31) % base
        

        source_hash, target_hash = 0, 0
        # calculate has for the target "bcd"
        for i in range(m):
            target_hash = (target_hash * 31 + ord(target[i])) % base

        for i in range(n):
            source_hash = (source_hash * 31 + ord(source[i]) ) % base

            if i < m - 1:
                continue

            # abc -a
            if i >= m:
                source_hash = source_hash - (ord(source[i - m]) * power) % base
                if source_hash < 0:
                    source_hash += base

            # abcd
            if source_hash == target_hash:
                # if hash is equal, then double check for each char
                # if hashes are not equal, the two strings will definitely not be the same
                # if the hashes are equal, the two strings may not be the same
                if source[i-m+1: i + 1] == target:
                    return i - m + 1

        return -1
