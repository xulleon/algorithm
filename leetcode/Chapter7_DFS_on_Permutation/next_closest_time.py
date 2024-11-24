from heapq import heappush, heappop
class Solution:
    def nextClosestTime(self, time: str) -> str:
        time = time[:2] + time[3:]
        results = []
        self.dfs(time, [], results)
        return self.find_next(results, time)
    
    def find_next(self, times, time):
        times.sort()
        index = times.index(time)
        while index < len(times) -1 and times[index] == times[index+1]:
            index += 1
        if index == len(times) -1:
            next = times[0]
        else:
            next = times[index + 1]

        return ''.join(next[:2] + ':' + next[2:])
        
    
    def dfs(self, time, subsets, results):
        time_dig = int(''.join(time))
        if len(subsets) == len(time):
            results.append(''.join(subsets))
            return
        
        for i in range(len(time)):                
            cnt = len(subsets)
        
            if cnt == 0:
                if 0 > int(time[i]) or int(time[i]) > 2:
                    continue
                 
            elif cnt == 1:
                if int(subsets[0]) == 2:
                    # filter out anything more than 24:00 inclusively
                    if 0 > int(time[i]) or int(time[i]) > 4:
                        continue
                else:
                    if 0 > int(time[i]) or int(time[i]) > 9:
                        continue
                
            elif cnt == 2:
                # filter out anything more than 24:00 inclusively
                if int(''.join(subsets[:2])) == 24:
                    continue
                # Filter out anything more than :60 inclusively
                if 0 > int(time[i]) or int(time[i]) > 6:
                    continue
                
            else:
                if subsets[2] == '6':
                    if int(time[i]) >= 0:
                        continue
                else:
                    if 0 > int(time[i]) or int(time[i]) > 9:
                        continue
                    
            subsets.append(time[i])      
            self.dfs(time, subsets, results)
            subsets.pop()
                   
                
