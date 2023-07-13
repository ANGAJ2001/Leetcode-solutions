class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        final = s.split()
        rev = final[::-1]
        return len(rev[0])
                

              

