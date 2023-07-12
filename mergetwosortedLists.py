# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1node = list1
        curr2node = list2
        final1 = [] 
        final2 = [] 
        while(curr1node!=None):
            final1.append(curr1node.val)
            curr1node = curr1node.next
        while(curr2node!=None):
            final2.append(curr2node.val)
            curr2node = curr2node.next
        
        final3 = final1+final2
        final3.sort()

        
        dummy = ListNode()
        currNode = dummy
        for i in final3:
            newNode = ListNode(i)
            currNode.next = newNode
            currNode = currNode.next
        
        return dummy.next

        
