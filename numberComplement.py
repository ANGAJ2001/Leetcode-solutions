class Solution:
    def findComplement(self, num: int) -> int:
        x = bin(num)
        p = ""
        xstr = str(x[2:])
        for i in xstr:
            if i == "1":
                p+="0"
            elif i == "0":
                p+="1"
        return int(p,2)
    
