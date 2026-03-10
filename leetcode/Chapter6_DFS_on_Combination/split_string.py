# https://www.lintcode.com/problem/680/
# Description:
# Given a string, you can split the string into substrings of (1) one character or (2) two characters. Return all possible combinations of substrings.
# Example:
# Input: "123"
# Output: [["1","2","3"], ["1","23"], ["12","3"]]

# Input: "12345"
# Output: [
#   ["1","2","3","4","5"],
#   ["1","2","3","45"],
#   ["1","2","34","5"],
#   ["1","23","4","5"],
#   ["1","23","45"],
#   ["12","3","4","5"],
#   ["12","3","45"],
#   ["12","34","5"]
# ]

def split_string(s):
    if s == '':
        return []
        
    results = []
    dfs(s, 0, [], results)
    return results
    
def dfs(s, index, subsets, results):
    if s == '' and len(subsets) != 1:
        results.append(subsets)
        
    for length in range(len(s)):
        prefix = s[: length + 1]
        
        
        subsets.append(prefix)
        print('length:', length, 'prefix:', prefix, 'subsets:', subsets)
        dfs(s[length+1:], length + 1, subsets[:], results)
        subsets.pop()
    
if __name__ == "__main__":
    s = '123456'
    a1 = split_string(s)
    print('a1:', a1)
