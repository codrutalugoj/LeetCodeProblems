class Solution:
    def jump(self, nums: list[int]) -> bool:
        # greedy solution, O(n) time complexity
        max_reach = 0
        num_jumps = 0

        l, r = 0, 0
        
        while r < len(nums) - 1:
            max_reach = 0
            for i in range(l, r + 1):
                max_reach = max(max_reach, i + nums[i])
            l = r + 1
            r = max_reach
            num_jumps += 1

        return num_jumps


if __name__ == "__main__":
    sol = Solution()
    nums1 = [2,3,1,1,4]
    nums2 = [1,2,1,1,1]
    print(sol.jump(nums1))
    print(sol.jump(nums2))
