class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0]* capacity
        self.size = 0
        self.capacity = capacity
       

    def get(self, i: int) -> int:
        
       return self.arr[i]

       

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1       


    def popback(self) -> int:

        value = self.arr[self.size-1]
        self.size -= 1
        return value
        

    def resize(self) -> None:
        newarr = [0]* (self.capacity *2)

        for i in range(self.size):
            newarr[i] = self.arr[i]

        self.arr = newarr
        self.capacity *= 2
       

    def getSize(self) -> int:
        return self.size
       
    
    def getCapacity(self) -> int:
        return self.capacity 
       