# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def convert_to_num(self, c) -> int:
        if c == "I":
            return 1
        elif c == "V":
            return 5
        elif c == "X":
            return 10
        elif c == "L":
            return 50
        elif c == "C":
            return 100
        elif c == "D":
            return 500
        elif c == "M":
            return 1000
    

    def romanToInt(self, s: str) -> int:
        romans = list(s)
        romans = list(map(self.convert_to_num, romans))
        number, i = 0, 0

        while i < len(romans)-1:
            if romans[i] < romans[i+1]:
                number += romans[i+1] - romans[i]
                i += 1
            else:
                number += romans[i]
            i += 1
        if i == len(romans)-1:
            number += romans[-1]
        return number
         


s = Solution()