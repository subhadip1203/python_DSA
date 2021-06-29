'''
link: https://leetcode.com/problems/length-of-last-word/

Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        length = 0
        while i >=0 :
            if s[i] == " ":
                if length > 0 :
                    return length
            else:
                length +=1
            i=i-1

        return length

        # wordlist = s.split()
        # if wordlist:
        #     return len(wordlist[-1])
        # return 0

s = "Hello World  "
print(Solution().lengthOfLastWord(s))

s = " "
print(Solution().lengthOfLastWord(s))