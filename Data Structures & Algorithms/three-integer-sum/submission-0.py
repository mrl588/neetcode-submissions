class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = 0
        result = []
        sortednums = sorted(nums)
        
        for i , num in enumerate(sortednums):

            if i > 0 and sortednums[i] == sortednums[i - 1]:
                continue

            left = i + 1
            
            right = len(nums) - 1 
            while left < right :
                s = sortednums[left] + num + sortednums[right]
                if s < 0 :
                    left += 1
                elif s > 0 :
                    right -= 1
                else:
                    result.append([num,sortednums[left] , sortednums[right]])
                    while left < right and sortednums[left] == sortednums[left + 1]:
                        left += 1
                    while left < right and sortednums[right] == sortednums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
        return result


        