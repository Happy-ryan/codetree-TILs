n = int(input())
cmds = [list(input().split()) for _ in range(n)]

def solution(n, cmds):
    dic = {}
    for cmd in cmds:
        do = cmd[0]
        if do == 'add':
            k, v = cmd[1], cmd[2]
            dic[k] = v
        elif do == 'find':
            k = cmd[1]
            if k in dic:
                print(dic[k])
            else:
                print('None')
        elif do == 'remove':
            k = cmd[1]
            dic.pop(k)

solution(n, cmds)