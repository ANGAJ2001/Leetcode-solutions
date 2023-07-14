from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studq = deque(students)
        sandq = deque(sandwiches)
        count = 0
        
        while studq and count < len(studq):
            if studq[0] == sandq[0]:
                studq.popleft()
                sandq.popleft()
                count = 0  # Reset the count when a student is served
            else:
                studq.append(studq.popleft())
                count += 1
                
        return len(studq)
