'''
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

 

Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
 

Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100
'''

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        char_inx = {}
        for i in range(len(s)):
            char_inx[i] = s[i]
        
        final_shift = []
        rs = 0
        ls = 0
        
        for item in shift:
            if item[0] == 0:
                ls += item[1]
            else:
                rs += item[1]
        if rs == ls:
            return s
        elif rs > ls:
            final_shift.append(1)
            final_shift.append(rs-ls)
        else:
            final_shift.append(0)
            final_shift.append(ls-rs)
        final_shift[1] = final_shift[1]%len(s)
        if final_shift[0] == 0:
            for i in range(len(s)):
                if i-final_shift[1] < 0:
                    j = len(s) + i - final_shift[1]
                else:
                    j = i - final_shift[1]
                char_inx[j] = s[i]
        else:
            for i in range(len(s)):
                if i+final_shift[1] >= len(s):
                    j =  i + final_shift[1] - len(s)
                else:
                    j = i + final_shift[1]
                char_inx[j] = s[i]
        return ''.join([v for k,v in sorted(char_inx.items())])
                    