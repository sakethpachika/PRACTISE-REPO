## Question 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        emp = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in emp:
                return [emp[diff],i]
            emp[j]=i
