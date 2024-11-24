# https://leetcode.com/problems/delete-characters-to-make-fancy-string


class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        prettyString = s[:2]
        for letter in s[2:]:
            if letter == prettyString[-1] and letter == prettyString[-2]:
                pass
            else:
                prettyString += letter
        return prettyString
        
        


print(Solution.makeFancyString(Solution, "leeetcode"))
print(Solution.makeFancyString(Solution, "aaabaaaa"))
print(Solution.makeFancyString(Solution, "aab"))