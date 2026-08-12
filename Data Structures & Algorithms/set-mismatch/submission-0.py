class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s1 = []
        res = []

        for i in range(len(nums)):
            if nums[i] not in s1:
                s1.append(nums[i])
            else:
                res.append(nums[i])   # duplicate

        for i in range(1, len(nums) + 1):
            if i not in s1:
                res.append(i)         # missing

        return res