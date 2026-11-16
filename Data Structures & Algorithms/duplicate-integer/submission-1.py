class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_seen =[]
        for i in nums:
            if i in is_seen:
                return True
            else:
                is_seen.append(i)
        return False

nums = [1,2,3,3]
s = Solution()
result = s.hasDuplicate(nums)
print(result)