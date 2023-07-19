class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            x = bin(i)
            xstr = str(x)
            count = 0
            for i in xstr:
                if i == '1':
                    count+=1
            res.append(count)
        return res
            
