class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        if k == 0:
            return [0] * n
            
        result = [0] * n

        extended = code + code
        
        for i in range(n):
            if k > 0:
                result[i] = sum(extended[i + 1:i + k + 1])
            else:
                result[i] = sum(extended[i + n + k:i + n])
                
        return result

        
        




print(Solution.decrypt(Solution,code = [5,7,1,4], k = 3))