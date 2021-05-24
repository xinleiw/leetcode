import time


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i, num in enumerate(nums):
            j = nums_dict.get(target - num)
            if j is not None and i != j:
                return [i, j]
            nums_dict[num] = i


if __name__ == '__main__':
    start = time.time()
    solution = Solution()
    result = solution.twoSum([3, 0,2,4,6,7,8,2,1,23,6,3], 6)
    end = time.time()
    print(end-start)
    print(result)
