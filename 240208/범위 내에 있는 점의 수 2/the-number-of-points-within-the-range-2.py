n, q = map(int, input().split())
dots = list(map(int, input().split()))
qs = [list(map(int, input().split()))for _ in range(q)]

inf = int(1e6)
pos = [0] * inf
for  dot in dots:
    pos[dot] = 1
psum = [0] * (inf + 1)

for i in range(inf):
    psum[i + 1] = pos[i] + psum[i]

for s, e in qs:
    print(psum[e + 1] - psum[s])