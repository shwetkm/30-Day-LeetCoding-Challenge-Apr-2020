'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_map = {}   
        curr_sum = 0 
        max_len = 0 
        ending_index = -1 
        n = len(nums)
        for i in range (0, n):  
            if(nums[i] == 0):  
                nums[i] = -1 
            else:  
                nums[i] = 1 

        for i in range (0, n):  

            curr_sum = curr_sum + nums[i]  

            if (curr_sum == 0):  
                max_len = i + 1 
                ending_index = i  
  
            if curr_sum in hash_map:
                if max_len < i - hash_map[curr_sum]: 
                    max_len = i - hash_map[curr_sum] 
                    ending_index = i 
            else:  
                hash_map[curr_sum] = i   

        for i in range (0, n):  
            if(nums[i] == -1):  
                nums[i] = 0 
            else:  
                nums[i] = 1 

        return max_len 