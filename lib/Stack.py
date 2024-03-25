class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return True if len(self.items) == 0 else False

    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            return None

    def pop(self):
        return self.items.pop() if len(self.items) != 0 else None

    def peek(self):
        return self.items[len(self.items)]
    
    def size(self):
        return len(self.items)

    def full(self):
        return True if len(self.items) >= self.limit else False

    def search(self, target):
        for i in reversed(range(len(self.items))):
            if self.items[i] == target:
                return len(self.items) -1  - i 
        return -1