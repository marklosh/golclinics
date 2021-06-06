class stack:
    def __init__(self):
        self.arr = []
    def push(self, element):
            self.arr.append(element)
    def pop(self):
        return self.arr.pop()

def reverse(string):
    s1 = stack()
    empty_string = "" 
    for letter in string:
        s1.push(letter)
    while len(s1.arr) != 0:
        empty_string += s1.pop()
    return empty_string
if __name__ == '__main__':
    s = stack()
    print(reverse("hey"))

    
            