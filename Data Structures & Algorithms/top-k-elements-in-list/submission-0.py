class Solution:
    def topKFrequent(self, nums, k):
        d = {}

        # Count frequency
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        res = []

        # Find the top k frequent elements
        while k > 0:
            maxi = 0
            ans = None

            for key in d:
                if d[key] > maxi:
                    maxi = d[key]
                    ans = key

            res.append(ans)
            del d[ans]
            k -= 1

        return res