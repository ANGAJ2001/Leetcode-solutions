class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1int = int(num1)
        num2int = int(num2)

        res = num1int*num2int
        return str(res)
