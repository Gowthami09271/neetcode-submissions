class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for num in nums1:
            ans = -1

            # Find num in nums2
            for i in range(len(nums2)):
                if nums2[i] == num:

                    # Search for next greater element
                    for j in range(i + 1, len(nums2)):
                        if nums2[j] > num:
                            ans = nums2[j]
                            break
                    break

            res.append(ans)

        return res