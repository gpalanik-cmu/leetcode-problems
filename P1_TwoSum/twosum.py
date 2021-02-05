class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_elements = len(nums)
        for i in range(num_elements):
            for j in range(i+1, num_elements):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
