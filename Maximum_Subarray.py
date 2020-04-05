'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

from sys import maxsize
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -maxsize - 1
        max_ending_here = 0
        start = 0
        end = 0
        s = 0

        for i in range(0,len(nums)): 

            max_ending_here += nums[i] 

            if max_so_far < max_ending_here: 
                max_so_far = max_ending_here 
                start = s 
                end = i 

            if max_ending_here < 0: 
                max_ending_here = 0
                s = i+1
        return max_so_far