class MinStack:
    stack = []
    min_stack  = None

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack is None or self.min_stack > val: 
            self.min_stack = val
        return None

    def pop(self) -> None:
        value = self.stack.pop()
        if len(self.stack) == 0:
            self.min_stack = None
        elif value == self.min_stack:
            self.min_stack = self.stack[0] 
            for i in range(1,len(self.stack)):
                if self.stack[i] < self.min_stack:
                    self.min_stack = self.stack[i] 
        return None

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return int(self.min_stack)
        
