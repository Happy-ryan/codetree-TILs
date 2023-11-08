s = input()
stack = []

for x in s:
    if not len(stack) or x == "(":
        stack.append(x)
    else:
        if stack[-1] == "(":
            stack.pop()

if not len(stack):
    print("Yes")
else:
    print("No")