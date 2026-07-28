class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # return len(set(nums)) != len(nums)

        hashed_set = set()

        for number in nums:
            if number in hashed_set:
                return True
            hashed_set.add(number)
        
        return False
             
        