# https://leetcode.com/problems/analyze-user-website-visit-pattern/
from itertools import combinations
from collections import defaultdict
import heapq
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_time_site = defaultdict(list)
        # create a dict to hold three info
        for user, time, site in zip(username, timestamp, website):
            user_time_site[user].append((time, site))

        # sort on time for each user list and create
        # generate a new dict site_freq
        site_freq = defaultdict(int)
        for user, time_sites in user_time_site.items():
            time_sites.sort(key=lambda pair: pair[0])
            # a list of ordered site list on timestamp
            tmp = [site for time, site in time_sites]
            for sites in set(combinations(tmp, 3)):
                site_freq[sites] += 1

        # wite site_freq available, now we need sort it
        # according to it freq by headq
        res = []
        for sites, freq in site_freq.items():
            heapq.heappush(res, (-freq, sites))

        return res[0][1]

