class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        b = ''
        for i in a[::-1]:
            b+=i
        if(a==b):
            return True
        return False
        
