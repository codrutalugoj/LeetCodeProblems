# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums) - 1 # why -1 here?

        while(left <= right):

            mid = left + (right - left)//2

            if nums[mid] == target:
                print(mid)
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        print(left)
        return left

sol = Solution()
sol.searchInsert([1,3,5,6],5)
sol.searchInsert([1,3,5,6],2)