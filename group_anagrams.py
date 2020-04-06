'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
from collections import Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        for item in strs:
            count = Counter(item) 
            code = ''
            for k,v in dict(sorted(count.items())).items():
                if k != ' ':
                    code += k+str(v)
            if code in word_map:
                word_map[code].append(item)
            else:
                word_map[code] = [item]
        return word_map.values()