class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxc = 1
        if len(num_set) == 0:
            return 0
        for num in nums:
            if (num-1) not in num_set:
                count = 1
                j = num + 1
                while j in num_set:
                    j += 1
                    count +=1
                if count > maxc:
                    maxc = count 
        return maxc

        