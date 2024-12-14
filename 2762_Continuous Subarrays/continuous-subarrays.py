class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # 用 slide window 的邏輯解題
        num_dict = {} # 紀錄 window 中出現過的合法數字及其數量
        start = 0 # window 的起始 index
        end = 0 # window 的結束 index
        count = 0 # 符合條件的 subarray 總數

        # NOTE: 如果數字符合條件，window 就會向右增加一個單位（即 end+1），如果不符合的話會向右減少一個單位（start+1）
        # NOTE: 每次向右增加一個單位時就統計一次目前的 window size 加回 subarray 總數中

        while end < len(nums):
            num_dict[nums[end]] = num_dict.get(nums[end], 0) + 1

            while max(num_dict) - min(num_dict) > 2:
                num_dict[nums[start]] -= 1
                if num_dict[nums[start]] == 0:
                    del num_dict[nums[start]]
                start += 1
            
            count += end - start + 1
            end += 1
        return count