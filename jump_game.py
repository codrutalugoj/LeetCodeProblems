import time

class Solution:
    def canReachLast(self, nums: list[int]) -> bool:
        """
        Recursive solution, exponential time complexity:
        if len(nums) == 1:
            return True
        
        can_jump = False
        if nums[0] == 0:
            return False
        
        for jump in range(nums[0], 0, -1):
            if jump < len(nums) and self.canReachLast(nums[jump:]):
                can_jump = True
                break

        return can_jump
        """

        # Greedy solution, O(n) time complexity

        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            
            max_reach = max(max_reach, i + nums[i])

            if max_reach >= len(nums) - 1:
                return True
        
        return True


    def canJump(self, nums: list[int]) -> bool:
        start = time.time()
        res = self.canReachLast(nums)
        return res, time.time() - start


if __name__ == "__main__":
    sol = Solution()
    nums1 = [2,3,1,1,4]
    nums2 = [3,2,1,0,4]
    nums3 = [2,0,0]
    nums4 = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    print(sol.canJump(nums1))
    print(sol.canJump(nums2))
    print(sol.canJump(nums3))
    print(sol.canJump(nums4))