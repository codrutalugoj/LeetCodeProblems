# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        result = ""

        min_str = min(strs, key=len)
        strs.remove(min_str)

        for i in range(len(min_str)):
            for s in strs:
                if i == len(s) or min_str[i] != s[i]:
                    return result
            result += min_str[i]
        return result


s = Solution()

print(s.longestCommonPrefix(["flower","flower","flower","flower"]))