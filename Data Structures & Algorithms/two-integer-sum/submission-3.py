class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        dct = {}
        
        for i in range(len(nums)):
            if target - nums[i] in dct.keys():
                return [dct[target - nums[i]], i]
            else:
                dct[nums[i]] = i