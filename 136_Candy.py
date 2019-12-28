'''
Accepted on leetcode(135)
time - O(N)
space - O(N)
Approach:
1. create an output array of same length as ratings array and initialize with all 1's.
2. then traverse the array from left then from right and increase the count accordingly.
3. then take the sum of elements to return minimum  count.

'''


class Solution:
    def candy(self, ratings) -> int:
        out = [1 for i in range(len(ratings))]

        # 1. left neighbour
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                out[i] = out[i - 1] + 1

        # 2. right neighbour
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                out[i] = max(out[i], out[i + 1] + 1)

        # 3. calculate sum
        sum = 0
        for i in range(len(out)):
            sum += out[i]

        return sum