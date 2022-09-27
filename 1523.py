# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/?envType=study-plan&id=programming-skills-i

class Solution:
    def countOdds(self, low: int, high: int) -> int:

        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2 
        return (high - low) // 2 + 1

sol = Solution()
print(sol.countOdds(3, 7)) # 3, 4, 5, 6, 7 -> 3, 5, 7
print(sol.countOdds(8, 10)) # 8, 9, 10 -> 9
print(sol.countOdds(14, 17)) # 15, 16, 17 -> 15, 17;   3/2=1; 