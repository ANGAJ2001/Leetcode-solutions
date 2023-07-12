# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currNode1 = l1
        s1 = ""
        while(currNode1!=None):
            s1+=str(currNode1.val)
            currNode1 = currNode1.next
        s1 = s1[::-1]
        print(s1)
        currNode2 = l2
        s2 = ""
        while(currNode2!=None):
            s2+=str(currNode2.val)
            currNode2 = currNode2.next
        s2 = s2[::-1]
        print(s2)
        
        
        s1int = int(s1)
        s2int = int(s2)
        print(s1int)
        print(s2int)
        finalsum = s1int+s2int
        finalS = str(finalsum)
        actualFinalS = finalS[::-1]
        print(actualFinalS)
        
        
        
        dummy = ListNode()  # Create a dummy node as the head of the linked list
        currNode = dummy
        
        for char in actualFinalS:
            newNode = ListNode(int(char))  # Create a new node with the integer value of the character
            currNode.next = newNode  # Set the next pointer of the current node to the new node
            currNode = currNode.next  # Move the current node pointer to the next node
        
        return dummy.next
        

        



        
        

