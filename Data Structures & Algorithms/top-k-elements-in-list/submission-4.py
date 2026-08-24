class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bank = {}
        for num in nums:
            bank[num] = 1 + bank.get(num,0)
        sortedbank = sorted(bank.items(), key = lambda bank: bank[1])

        return [num[0] for num in sortedbank[-k:]]
