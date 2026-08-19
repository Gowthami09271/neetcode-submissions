class Solution:
    def timeRequiredToBuy(self, tickets, k):
        queue = []

        for i in range(len(tickets)):
            queue.append([tickets[i], i])

        time = 0

        while queue:
            x = queue.pop(0)

            x[0] -= 1
            time += 1

            # Target person finished
            if x[1] == k and x[0] == 0:
                break

            # Person still has tickets
            if x[0] > 0:
                queue.append(x)

        return time