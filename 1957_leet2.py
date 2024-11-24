# https://leetcode.com/problems/maximum-matrix-sum/submissions/1461700732/?envType=daily-question&envId=2024-11-24

class Solution(object):
    def maxMatrixSum(self, matrix):
        n = len(matrix)
        
        count_negative = 0
        min_abs = float('inf')
        total_sum = 0
        
        for i in range(n):
            for j in range(n):
                total_sum += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    count_negative += 1
                min_abs = min(min_abs, abs(matrix[i][j]))
        
        if count_negative % 2 == 1:
            total_sum -= 2 * min_abs
            
        return total_sum


print(Solution().maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]))