# https://www.lintcode.com/problem/680/
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
