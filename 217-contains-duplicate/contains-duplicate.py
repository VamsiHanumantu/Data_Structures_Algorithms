class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans_set = set()
        for num in nums:
            if num in ans_set:
                return True
            ans_set.add(num)
        return False