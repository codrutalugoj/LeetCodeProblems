# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        # hashmap with 
        # -> values = (prefix prod, suffix prod)
        # -> keys = index??
        # E.g. nums = [1,2,3,4]; 
        answer = [1 for _ in range(len(nums))]
        curr_suffix_val = 1

        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            curr_suffix_val *= nums[i+1]
            answer[i] *= curr_suffix_val
            
        return answer
        
prodC = Solution()
print(prodC.productExceptSelf([1,2,3,4]))
print(prodC.productExceptSelf([-1,1,0,-3,3]))
