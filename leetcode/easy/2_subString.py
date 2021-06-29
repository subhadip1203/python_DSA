'''
link: https://leetcode.com/problems/implement-strstr/

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length_haystack = len(haystack)
        length_niddle = len(needle)

        if length_niddle == 0:
            return 0
        elif length_haystack == length_niddle:
            if haystack == needle :
                return 0
            else:
                return -1
        
        for i in range(length_haystack-length_niddle+1) :
            if haystack[i] != needle[0]:
                continue
            elif haystack[i:i+length_niddle] == needle:
                return i
        return -1

haystack = "hello"
needle = "ll"
print(Solution().strStr(haystack,needle))

haystack = "aaaaa"
needle = "bba"
print(Solution().strStr(haystack,needle))

haystack = "a"
needle = "a"
print(Solution().strStr(haystack,needle))

haystack = "a"
needle = ""
print(Solution().strStr(haystack,needle))

haystack = "abc"
needle = "c"
print(Solution().strStr(haystack,needle))