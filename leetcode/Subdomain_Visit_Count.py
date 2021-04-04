# https://leetcode.com/problems/subdomain-visit-count/
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        from collections import defaultdict
        cpdomains = [k.split() for k in cpdomains]
        cpdict = defaultdict(int)
        for cpd in cpdomains:
            visited = int(cpd[0])
            domains = cpd[1].split('.')
            while domains:
                cpdict['.'.join(domains)] += visited
                domains.pop(0)

        res = [' '.join([str(v), k]) for k, v in cpdict.items()]
        return sorted(res, key= lambda grp: (grp[0], len(grp[1])))
