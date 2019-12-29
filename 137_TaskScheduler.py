'''
Accepted on leetcode(621)
time - O(N)
space - O(N), max of 3N if all given tasks are same.
'''


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        # character array
        noOfTasks = [0 for i in range(26)]  # declare a character array

        for ch in tasks:
            noOfTasks[ord(ch) - ord('A')] += 1  # input count of occurance

        noOfTasks = sorted(noOfTasks)  # sort in ascending order
        count = 0
        time = 0

        while noOfTasks[25] > 0:  # while the last array element is greater than 1.
            while noOfTasks[25] > 0 and count <= n:
                if count < 26 and noOfTasks[25 - count] > 0:
                    # checking for valid process where count is greater than 0.
                    noOfTasks[25 - count] -= 1
                count += 1
                time += 1
            count = 0  # reinitialize count for each CPU cycle.
            noOfTasks = sorted(noOfTasks)

        return time