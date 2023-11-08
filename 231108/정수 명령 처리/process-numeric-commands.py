class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def top(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items[-1]


s = Stack()
cmd_num = int(input())
for _ in range(cmd_num):
    cmd = list(input().split())
    if cmd[0] == "push":
        s.push(cmd[1])
    else:
        if cmd[0] == "size":
            print(s.size())
        elif cmd[0] == "empty":
            print(1 if s.empty() else 0)
        elif cmd[0] == "pop":
            print(s.pop())
        elif cmd[0] == "top":
            print(s.top())