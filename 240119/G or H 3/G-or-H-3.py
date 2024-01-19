n, k = map(int, input().split())
people = [list(input().split()) for _ in range(n)]

scores = [0] * 10001
for x, score in people:
    x = int(x)
    if score == 'G':
        scores[x] = 1
    else:
        scores[x] = 2


max_val = 0
for i in range(1, 10001 - k):
    score_val = 0
    for j in range(i, i + k + 1):
        score_val += scores[j]

    max_val = max(score_val, max_val)

print(max_val)