n, m, k = map(int, input().split())
move_numbers = list(map(int, input().split()))

# board - 공의 시작점이 1부터 시작이다!
# board의 각 인덱스가 공의 좌표를 의미한다.
# 1번에서 시작하기 때문에 board의 초기값은 1로 설정하는 것이 맞다.
# 1로 설정했을 때 m 이 1인 경우 공들이 아예 못 움직이는 경우가 있다.
# 그러므로 0으로 설정하되 판단할 때 m 이 아니라 m - 1로 판단하는 것이 괜찮아 보인다.
board = [0 for _ in range(k + 1)]

# 움직임이 이미 정해져있을 때 말들을 선택할 수 있는 조합을 만들고 최대 점수를 먹는 것!
# 각 말은 1 1 1  / 1 2 1 ...이렇게 선택될 수 있다. > 중복순열
# simple유형이라고 생각할 수 있지만 이미 m번으로 이동한 말의 경우 점수에 영향을 주지 못하고 이동횟수만 소진하게 된다.
# 따라서 m에 도착한 말은 선택되지 않도록 경우의 수를 생성해야한다. (conditional)
# 중복조합 + conditional

# board에 move_number에 따른 공의 좌표를 기록한다. ans필요없음!
max_score = 0
def dfs(level):
    global max_score
    if level == n:
        sum_val = sum([1 for x in board if x >= m - 1])
        # print(f"sum_val: {sum_val}, board: {board}")
        max_score = max(max_score, sum_val)
        return
    
    for cur_dice in range(1, k + 1):
        # conditional
        # if board[cur_dice] >= m:
        #     continue
        board[cur_dice] += move_numbers[level]
        dfs(level + 1)
        board[cur_dice] -= move_numbers[level]

# k = 1일때 level == n에 안들어감...왜?

dfs(0)
print(max_score)