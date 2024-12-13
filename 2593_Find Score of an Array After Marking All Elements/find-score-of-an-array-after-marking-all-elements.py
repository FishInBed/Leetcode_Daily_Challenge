class Solution:
    def findScore(self, nums: List[int]) -> int:
        sort_list = [(num, idx) for idx, num in enumerate(nums)]
        sort_list.sort()
        mark_list = [False]*len(nums)
        score = 0

        for i in range(len(nums)):
            idx = sort_list[i][1]
            num = sort_list[i][0]
            if mark_list[idx] is not True:
                score += num
                mark_list[idx] = True
                if idx > 0:
                    mark_list[idx-1] = True
                if idx < len(nums)-1:
                    mark_list[idx+1] = True
        return score