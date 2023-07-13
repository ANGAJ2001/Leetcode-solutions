class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = []
        num = []
        a = ""
        for i in digits:
            s.append(str(i))
        for i in s:
            a+=i
        b = int(a)
        c = b+1
        d = str(c)
        for i in range(len(d)):
            num.append(int(d[i]))
        return num

        
