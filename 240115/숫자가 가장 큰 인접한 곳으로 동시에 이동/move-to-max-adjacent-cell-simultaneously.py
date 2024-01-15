from collections import Counter

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 초기pos는 1base고 new_pos 0base > 둘이 맞춰야함.
# move할 때 초기 pos를 0base로 바꾸기 위해서 r - 1, c - 1을 하는데 그러면 그 이후 new_pos부터는 0base임에도 -1을 하게 됨.
def change_0base(pos):
    new_pos = []
    for r, c in pos:
        new_pos.append([r - 1, c - 1])
    return new_pos


def in_range(r, c):
    return 0 <= r < n and 0 <= c < n


def move(r, c):
    final_dir = 0
    final_val = 0
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if in_range(nr, nc) and board[nr][nc] > final_val :
            # 상하좌우로 미리 dr,dc를 설정함
            # 따라서 같은 값이 4개 나오더라도 >= 하지 않아서 우선순위대로 움직이게 된다!
            final_val = board[nr][nc]
            final_dir = (nr, nc)
    return final_dir


def one_time_move_all():
    global pos
    new_pos_candidate = []

    for r, c in pos:
        final_dir = move(r, c)
        new_pos_candidate.append(final_dir)
    
    # 중복되는 곳 지우기
    dic = Counter(new_pos_candidate)
    new_pos = [key for key, count in dic.items() if count == 1]
    pos = new_pos
    
    return pos


n, m, t = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
pos = change_0base([list(map(int, input().split())) for _ in range(m)])

# pos가 계속 변경
def simulate():
    for _ in range(t):
        one_time_move_all()
    
    return len(pos)


print(simulate())