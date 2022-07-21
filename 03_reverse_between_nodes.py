class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        if self.next:
            return f"{self.val}->{self.next}"
        return f"{self.val}"


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data):
        new_node = ListNode(data)
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        else:
            self.head = new_node

    def __repr__(self) -> str:
        return f"{self.head}"


def reverse_between_nodes(head: ListNode, left: int, right: int) -> ListNode:
    if not head:
        return None

    cur, prev = head, None
    while left > 1:
        prev = cur
        cur = cur.next
        left, right = left - 1, right - 1

    tail, con = cur, prev

    while right:
        third = cur.next
        cur.next = prev
        prev = cur
        cur = third
        right -= 1

    if con:
        con.next = prev
    else:
        head = prev
    tail.next = cur

    return head


ln1 = LinkedList()
for i in range(1, 11):
    ln1.insert(i)

print(ln1)
print(reverse_between_nodes(ln1.head, 2, 6))
