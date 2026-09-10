class Node:
    def __init__(self, val):
      self.val = val
      self.next = None

       
class LinkedList:
    
    def __init__(self):
        self.head = None
      

    def get(self, index: int) -> int:
        curr = self.head
        i = 0

        while curr:
            if i == index:
                return curr.val

            curr = curr.next
            i += 1

        return -1        



      
    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

             

        
      
    def insertTail(self, val: int) -> None:
        newNode = Node(val)

        if self.head == None:
            self.head = newNode
            return 

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = newNode   
       

    def remove(self, index: int) -> bool:

        if not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        i = 0
        curr = self.head    

        while curr and i < index-1:
            curr = curr.next
            i += 1

        if not curr or not curr.next:
            return False

        curr.next = curr.next.next
        return True        



       

    def getValues(self) -> List[int]:
        current = self.head
        values = []

        while current:
            values.append(current.val)
            current = current.next
        return values    






      
