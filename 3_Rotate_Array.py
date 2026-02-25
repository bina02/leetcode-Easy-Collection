# Solution1(insert), time_complexity = O(n*k)
import time

class Solution(object):
    def rotate(self, nums, k):
        for i in range(k):
            last_num = nums.pop(-1)
            nums.insert(0, last_num)
        return nums

start = time.time()

nums = [1,2,3,4,5,6,7,8,9,10]
k = 100000000
solution = Solution()
print(solution.rotate(nums, k))

end = time.time()
print(end - start)