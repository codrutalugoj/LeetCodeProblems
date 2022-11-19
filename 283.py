# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Main idea: Search for non-zero elems with the right pointer and swap that elem with a zero elem 
        that the left pointer is pointed to.
        """
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0 and nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left] !=0:
                left += 1
        print(nums)

sol = Solution()
sol.moveZeroes([2,6,0,7,4,0,0])