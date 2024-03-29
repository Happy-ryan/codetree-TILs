n, m = map(int, input().split())
strings = [input() for _ in range(n)]
qs = [input() for _ in range(m)]

def solution(n, m, strings, qs):
    dic1 = {}
    dic2 = {}
    for idx, s in enumerate(strings):
        dic1[s] = idx + 1
        dic2[idx + 1] = s

    for q in qs:
        if q.isdigit():
            print(dic2[int(q)])
        else:
            print(dic1[q])


solution(n, m, strings, qs)