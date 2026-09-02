#Given a string s, find the length of the longest substring without duplicate characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        global_max = 0
        substring = []
        for character in s:
            if not character in substring:
                substring.append(character)
            else:
                substring = substring[substring.index(character)+1:]
                substring.append(character)
            global_max = max(len(substring), global_max)
        return global_max