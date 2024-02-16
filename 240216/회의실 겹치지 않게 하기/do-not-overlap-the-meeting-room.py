n = int(input())
cmds = [list(map(int, input().split())) for _ in range(n)]
# 회의실
# 끝나는 시간이 이를수록 더 많은 회의를 넣을 수 있다.
# 취소를 최소...회의를 최대화!!
# 시작시간도 빠르게!
cmds.sort(key=lambda x: (x[1], x[0]))

last = cmds[0][1]
cnt = 1
for start, end in cmds[1:]:
    if last <= start:
        cnt += 1
        last = start

print(n - cnt)