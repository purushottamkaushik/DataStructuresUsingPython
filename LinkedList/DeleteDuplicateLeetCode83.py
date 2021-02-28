class Node:
    def __init__(self,data):
        self.info = data
        self.next = None

class LinkedListV2:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
        temp = self.head
        while temp:
            print(temp.info,end=" ")
            temp = temp.next
        print()

    def insertAtEnd(self,data):
        self.data = Node(data)
        if self.head is None:
            self.head = self.data
        else:
            currNode  = self.head # head refers to the first node
            while currNode.next is not None:
                currNode = currNode.next
            currNode.next = self.data


def deleteduplicate(head):
    dummy = Node(head.info)
    dummy.next = head

    current = head
    while current.next is not None:
        if current.info == current.next.info:
               current.next = current.next.next
        else:
            current = current.next
    return dummy.next

if __name__=="__main__":
    list = LinkedListV2()
    list.insertAtEnd(0)
    list.insertAtEnd(0) # Insert at the end
    list.insertAtEnd(0)
    list.insertAtEnd(0)
    list.insertAtEnd(0)

    list.display()

    lst = deleteduplicate(list.head)

    while lst:
        print(lst.info,sep=" " ,end=" ")
        lst = lst.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#
#         dummy = ListNode(0)
#         dummy.next = head
#
#         current = head
#         while current:
#             if current.next is not None and current.val == current.next.val:
#                 current.next = current.next.next
#             else:
#                 current = current.next
#         return dummy.next