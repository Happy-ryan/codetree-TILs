from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)
    
    def empty(self):
        return not self.dq

    def size(self):
        return len(self.dq)

    def pop(self):
        if self.empty():
            raise Exception("Queue is empty!")

        return self.dq.popleft()

    def front(self):
        if self.empty():
            raise Exception("Queue is empty!")
        return self.dq[0]


q = Queue()
n = int(input())
for _ in range(n):
    cmds = list(input().split())
    if cmds[0] == "push":
        q.push(cmds[1])
    elif cmds[0] == "front":
        print(q.front())
    elif cmds[0] == "size":
        print(q.size())
    elif cmds[0] == "pop":
        print(q.pop())
    else:
        print(1 if q.empty() else 0)