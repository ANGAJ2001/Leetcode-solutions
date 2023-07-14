# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        currNode = head
        l = []
        while(currNode!=None):
            if currNode.next in l:
                return True
            l.append(currNode)
            currNode = currNode.next
        return False
            
        
