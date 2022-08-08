# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.


class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum=nums[0]
        curr_sum=0
        for x in nums:
            if curr_sum<0:
                curr_sum=0
            curr_sum+=x
            max_sum = max(max_sum,curr_sum)
        return max_sum
if __name__ =='__main__':
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    Sol = Solution()
    result = Sol.maxSubArray(nums)
    print(result)
