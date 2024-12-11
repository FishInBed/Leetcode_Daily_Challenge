class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        size = 0
        for num in nums:
            if num - nums[size] > 2*k:
                size += 1
        return len(nums) - size