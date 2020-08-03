from typing import List

#Time O(n2)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        for i in range(len(nums)):
            swapped = False
            for j in range(len(nums)-i-1):
                if nums[j] >= nums[j+1]:
                    self.swap(nums,j , j+1)
                    swapped = True
            if not swapped:
                break
        return nums

    def swap(self, nums, x, y):
        tmp = nums[x]
        nums[x] = nums[y]
        nums[y] = tmp

test = Solution()
print(test.sortArray([6,2,1,9,8]))