class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=0
        total_sum=sum(nums)
        res=0
        for i in range(0,len(nums)):
            left_sum=sum(nums[:i])
            right_sum=total_sum-left_sum-nums[i]
            if left_sum==right_sum:
                return i
        return -1
        

        