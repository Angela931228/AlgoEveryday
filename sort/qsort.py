from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        self.qsort(nums, 0, len(nums) - 1)
        return nums

    def qsort(self, nums: List[int], start, end):
        if start <= end:
            p = self.partition(nums, start, end)
            self.qsort(nums, start, p - 1)
            self.qsort(nums, p + 1, end)

    def partition(self, nums: List[int], start, end):
        p = nums[end]
        i = start
        for j in range(start, end):
            if nums[j] < p:
                self.swap(nums, i, j)
                i = i + 1
        self.swap(nums, i, end)
        return i

    def swap(self, nums: List[int], x, y):
        tmp = nums[x]
        nums[x] = nums[y]
        nums[y] = tmp

test = Solution()
test.sortArray([3,5,6,7,8])