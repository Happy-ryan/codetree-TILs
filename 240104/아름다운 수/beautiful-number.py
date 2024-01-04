n = int(input())

def is_beautiful_number(number):
    s = 0
    while s < len(number):
        if number[s] == '1':
            s += 1
        elif number[s] == '2':
            if s + 1 < len(number) and number[s + 1] == '2':
                s += 2
            else:
                return False
        elif number[s] == '3':
            if s + 2 < len(number) and number[s + 1] == '3' and number[s + 2] == '3':
                s += 3
            else:
                return False
        else:
            if s + 3 < len(number) and number[s + 1] == '4' and number[s + 2] == '4' and number[s + 3] == '4':
                s += 4
            else:
                return False
    return True

cnt = 0
res = []
def dfs(idx):
    global cnt
    if idx == n:
        if is_beautiful_number(res.copy()):
            cnt += 1
        return

    for i in ['1', '2', '3', '4']:
        res.append(i)
        dfs(idx + 1)
        res.pop()

dfs(0)

print(cnt)