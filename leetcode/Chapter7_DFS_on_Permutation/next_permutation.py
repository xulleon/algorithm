# https://leetcode.com/problems/next-permutation/
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Next Permutation.
# Memory Usage: 16.6 MB, less than 74.32% of Python3 online submissions for Next Permutation.
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        The "Next Permutation" problem on LeetCode involves rearranging
        numbers to form the next lexicographically larger permutation. 
        If no larger permutation is possible, rearrange it to the 
        smallest permutation (sorted in ascending order). A DFS approach 
        isn't the most optimal here, but a direct algorithm is preferred for efficiency.
        
        step 1 and 2: The idea is to use two pointers i, and j. one of the value is better than another.
        step 3: after swap the two elements, the changed value should be greater than the original value
        step 4: further reversed the rest value after ith element, to make even smaller than the value after step3.
        """
        # now i = 3, which points to 5
        n = len(nums)
        # Step1: find the first decreaseing number from right
        # i = n-2 is because, it need to compare i and i + 1
        # Therefore, find from the second from the last
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # now i = 3, which points to 5
        
        if i >= 0: #if this number exists
            # Step 2, find first larger number to the right of nums[i]
            #.        find from the last nuber
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # j is 5, which points to 6
            # step 3: swap the ith and jth elements. [1,2,3,6,7,5,4]
            
            # step 3: swap the ith and jth elements
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: revert the  sublist after i+1 inclusively. [1,2,3,6,4,5,7]
        nums[i+1:] = nums[i+1:][::-1]
        
        return nums
