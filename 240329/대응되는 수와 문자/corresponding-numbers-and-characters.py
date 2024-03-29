n, m = map(int, input().split())
strings = [input() for _ in range(n)]
qs = [input() for _ in range(m)]

def solution(n, m, strings, qs):
    dic = {}
    for idx, s in enumerate(strings):
        dic[s] = idx + 1

    for q in qs:
        if q.isdigit():
            print(strings[int(q) - 1])
        else:
            print(dic[q])


solution(n, m, strings, qs)