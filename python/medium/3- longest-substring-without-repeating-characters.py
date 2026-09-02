#Given a string s, find the length of the longest substring without duplicate characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        substring = []
        for character in s:
            if not character in substring:
                substring.append(character)
                max = len(substring) if len(substring) > max else max
            else:
                substring = substring[substring.index(character)+1:]
                substring.append(character)
        max = len(substring) if len(substring) > max else max
        return max