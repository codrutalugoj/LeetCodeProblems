# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        while nums.count(0) != 0:
            nums.remove(0)
            zeros.append(0)

        nums.extend(zeros)
        print(nums)

sol = Solution()
sol.moveZeroes([2,6,0,7,4,0,0])