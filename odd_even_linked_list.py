# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        first_even = head.next
        last_odd = head
        last_even = head.next
        curr = head.next.next

        while curr and curr.next:
            last_odd.next = curr
            last_even.next = curr.next

            last_odd = curr
            last_even = curr.next
            # move 2 nodes
            curr = curr.next.next

        if curr:
            last_odd.next = curr
            last_odd = curr
        last_odd.next = first_even
        last_even.next = None
        
        return head
    
    def printList(self, head: Optional[ListNode]):
        if not head:
            return
        
        self.printList(head.next)
        print(head.val)
    
if __name__ == "__main__":
    sol = Solution()
    #ex = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
    ex = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
    #head = sol.oddEvenList(ex)
    
    sol.printList(ex)
