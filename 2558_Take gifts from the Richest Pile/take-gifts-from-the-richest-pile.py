class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        temp_gift = sorted(gifts, reverse=True)
        for i in range(k):
            temp_gift[0] = int(temp_gift[0]**0.5)
            temp_gift.sort(reverse=True)
        return sum(temp_gift)