n, m = map(int, input().split())
res = []

def choose(idx):
    if idx == m:
        print(*res)
        return
    
    for i in range(1, n + 1):
        res.append(i)
        choose(idx + 1)
        res.pop()


choose(0)