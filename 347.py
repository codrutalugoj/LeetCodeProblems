# https://leetcode.com/problems/top-k-frequent-elements/
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # make a haskmap with all unique num in nums and assign the values to 0
        nums_hmap = {num: 0 for num in nums}

        # increment the value when we find an instance
        for num in nums:
            nums_hmap[num] += 1

        # sort the dict by the last k values
        dict_topk = sorted(nums_hmap.items(), key=lambda item: item[1])[-k:]

        # return only the keys in a list
        return [item[0] for item in dict_topk]
    
sol = Solution()
nums = [1,1,1,2,2,3]

print(sol.topKFrequent(nums, 2))

