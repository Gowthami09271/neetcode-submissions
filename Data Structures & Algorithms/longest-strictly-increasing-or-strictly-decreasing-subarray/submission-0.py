class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        s_in=1
        s_de=1
        res=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                s_in+=1
                s_de=1

            elif nums[i]<nums[i-1]:
                s_de+=1
                s_in=1
            else:
                s_in=1
                s_de=1
            res = max(res,s_in,s_de)
        return res
        