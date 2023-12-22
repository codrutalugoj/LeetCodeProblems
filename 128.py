# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        # go through all values and check if that value is the start of a sequence
        # e.g. nums = [100, 4, 200, 1, 3, 2]
        # 100 -> start of sequence; 

        nums_set = set(nums)
        longest_seq = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                length = 0
                while (num + length) in nums_set:
                    length += 1
                longest_seq = max(longest_seq, length)

        return longest_seq
