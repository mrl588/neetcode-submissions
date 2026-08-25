class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
  
        bank = {}
        for i in range(len(nums)):
            bank[nums[i]] = i 
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in bank.keys() and bank[difference] != i:
                if bank[difference] < i:
                    return [bank[difference], i]
                else:
                    return [i, bank[difference]]
                

