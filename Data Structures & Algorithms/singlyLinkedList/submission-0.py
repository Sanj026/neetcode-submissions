class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        cur = self.head
        i = 0
        while cur and i < index - 1:
            cur = cur.next
            i += 1
        if not cur or not cur.next:
            return False
        cur.next = cur.next.next
        return True

    def getValues(self) -> List[int]:
        result = []
        cur = self.head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result
