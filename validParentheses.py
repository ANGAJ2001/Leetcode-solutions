class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")":"(","]":"[","}":"{"}
        for i in s:
            if i in brackets.values():
                stack.append(i)
            elif stack and brackets[i] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return stack == []

