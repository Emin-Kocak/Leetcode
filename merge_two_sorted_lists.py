# Definition for singly-linked list.
class listNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object): 
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = listNode(0)
        current = temp
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return temp.next

def build_linked_list(values):
    head = listNode(0)
    current = head
    for val in values:
        current.next = listNode(val)
        current = current.next
    return head.next

# usage example:
liste1 = build_linked_list([1, 2, 3])
liste2 = build_linked_list([1, 3, 4])
merged_list = Solution().mergeTwoLists(liste1, liste2)
print(merged_list)
        

