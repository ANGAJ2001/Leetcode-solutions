from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        i = 0
        
        while(tickets[k]!=0):
            if i == len(tickets):
                i = 0
            if tickets[i]>1:
                tickets[i]-=1
                count+=1
            elif tickets[i] == 1:
                tickets[i] = 0
                count+=1
            i+=1
        return count

            

