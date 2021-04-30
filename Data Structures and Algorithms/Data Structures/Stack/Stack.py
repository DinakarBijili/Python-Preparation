"""
A stack is an ordered list in which insertion and deletion are done at one end, called top.
The last element inserted is the first one to be deleted.
Hence, it is called the Last in First out (LIFO). (FROM TOP)

Push: O(1)
Pop: O(1)
Peek: O(1)
isEmpty: O(1)
Size: O(1)
"""

class Stack(object):
    def __init__(self, limit = 10):
        self.stack = []
        self.limit = limit
    
    # for printing the stack contents
    def __str__(self):
        return ' '.join([str(i) for i in self.stack])
    
    # for pushing an element on to the stack
    def push(self, data):
        if len(self.stack) >= self.limit:
            print('Stack Overflow')
        else:
            self.stack.append(data)
            
    # for popping the uppermost element
    def pop(self):
        if len(self.stack) <= 0:
            print('Stack Underflow')
        else:
            self.stack.pop()
            
    # for peeking the top-most element of the stack
    def peek(self):
        if len(self.stack) <= 0:
            print('Stack Underflow')
        else:
            return self.stack[-1]
        
    # to check if stack is empty
    def isEmpty(self):
        return len(self.stack) == 0
    
    # for checking the size of stack
    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    myStack = Stack()
    for i in range(10):
        myStack.push(i)
    print(myStack)
    myStack.pop()            # popping the top element
    print(myStack)
    myStack.peek()          # printing the top element
    print("Peek",myStack)
    myStack.isEmpty()
    print("Empty", myStack)
    myStack.size()
    print("Size", myStack)

#OUTPUT:-
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8