# Chocolate Distribution Problem
class Solution:

    def findMinDiff(self, A,N,M):

        A.sort()
        left = 0
        right = M-1
        diff = A[right]-A[left]
        while right<len(A):
            diff = min(diff, A[right]-A[left])
            left+=1
            right+=1
        return diff