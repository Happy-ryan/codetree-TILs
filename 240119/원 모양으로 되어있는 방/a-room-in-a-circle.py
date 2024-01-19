n = int(input())
# 모든 사람이 같은 방에서 출발!
# 어디 방에서 출발해야 거리의 합이 최소가 되냐!
# 반드시 시계 방향
people = [int(input()) for _ in range(n)]

# 방을 회전시킬 것!
def choose_first_room(people):
    dist = 0
    for idx, number in enumerate(people):
        dist += idx * number
    return dist


total_dist = 100000000

for _ in range(n):
    people = people[1:] + [people[0]]
    cur_dist = choose_first_room(people)
    total_dist = min(total_dist, cur_dist)

print(total_dist)