n = int(input())
s1 = input()
s2 = input()

ans = []
cnt = 0
for i in range(n):
    if s1[i] != s2[i]:
        cnt += 1
    else:
        if cnt != 0:
            ans.append(cnt)
        cnt = 0

if cnt != 0:
    ans.append(cnt)

print(len(ans))