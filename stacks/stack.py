class Stack:
    def __init__(self, initial_size):
        self.arr = [0 for _ in range(initial_size)]
        self.top = -1
        self.num_of_elements = 0
    def push(self, value):
        if self.top + 1 == len(self.arr):
            print("stack overflow, adding some space for extra element(s)")
            self.handle_full_capacity()
        self.top += 1
        self.arr[self.top] = value
        self.num_of_elements += 1
    def handle_full_capacity(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(len(old_arr) * 2)]
        for index, element in enumerate(old_arr):
            self.arr[index] = element
    def pop(self):
        if self.is_empty():
            print("stack undeflow")
            self.top = -1
            return None
        self.num_of_elements -= 1
        return self.arr[self.num_of_elements]
        self.top = self.top - 1
    def is_empty(self):
        return self.num_of_elements == 0
    def capacity(self):
        return self.top + 1
    def size(self):
        return len(self.arr)
    def peek(self):
        return self.arr[self.top]

if __name__ == '__main__':
    #print(reverse("losh"))
    s = Stack(10)
    for num in range(100):
        s.push(num)
    for i in range(101):
        print(s.pop())
    print(s.arr)



    
    
