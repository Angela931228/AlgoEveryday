from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        self.mergeSort(nums,0,len(nums)-1)
        return nums
    def mergeSort(self, nums: List[int], start: int, end: int):
        if start< end:
            mid = (start + end) // 2
            self.mergeSort(nums, start, mid)
            self.mergeSort(nums, mid+1, end)
            self.merge(nums, start, mid, end)

    def merge(self, nums: List[int], start: int, mid: int, end: int):
        l_array = nums[start:(mid+1)]
        r_array = nums[mid+1:end+1]
        i, j, k = 0, 0, 0
        while i < len(l_array) and j < len(r_array):
            if r_array[j] < l_array[i]:
                nums[start+k] = r_array[j]
                k = k + 1
                j = j + 1
            elif r_array[j] >= l_array[i]:
                nums[start+k] = l_array[i]
                k = k + 1
                i = i + 1
        if i < len(l_array):
            nums[start+k:end+1] = l_array[i:]
        elif j < len(r_array):
            nums[start+k:end+1] = r_array[j:]

test = Solution()
print(test.sortArray([6,2,1,9,8]))