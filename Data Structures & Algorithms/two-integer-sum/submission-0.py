class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i in range(0,len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return list((seen[complement], i))
            else:
                seen[nums[i]] = i

sol = Solution()
nums = [3,4,5,6]
target = 7
result = sol.twoSum(nums, target)