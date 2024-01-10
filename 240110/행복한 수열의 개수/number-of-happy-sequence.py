# 시간복잡도: O(N)
def is_happy(arr: list[int], m):
    start = arr[0]
    # start도 개수에 포함!
    cnt = 1
    for number in arr[1:]:
        if number == start:
            cnt += 1
        else:
            # 연속하지 않으면 start가 갱신되어야함.
            cnt = 1
            start = number
        # 넘는 순간 종료
        if cnt >= m:
            return True
    return False

def extract_row(board: list[list[int]]):
    res = []
    # 행 추출
    for r in range(n):
        res.append(board[r])
    # 열 추출
    for c in range(n):
        row = []
        for r in range(n):
            row.append(board[r][c])
        res.append(row)

    return res    
# 시간복잡도: 수열고르기(O(N)) * 행복수열(O(N))
def solution(n: int, m: int, board: list[list[int]]):
    if n == 1:
        return 2
    res = extract_row(board)
    cnt = 0
    for row in res:
        # print(row)
        if is_happy(row, m):
            cnt += 1
    return cnt
        
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, board))