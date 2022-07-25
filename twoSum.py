from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    comp_dict = dict()
    for i in range(len(nums)):
        val = nums[i]
        comp = target - val
        if comp in comp_dict:
            return [comp_dict[comp], i]

        comp_dict[val] = i
print(twoSum([1, 2, 3], 4))        # [0, 2]
print(twoSum([2, 7, 11, 15], 9))   # [0, 1]
print(twoSum([3, 2, 4], 6))        # [1, 2]
print(twoSum([3, 3], 6))           # [0, 1]

print(twoSum([1,3,6,7], 10))
print(twoSum([1,5,6,7], 13))
print(twoSum([3,5,8,9,12], 14))