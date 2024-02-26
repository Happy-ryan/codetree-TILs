n = int(input())

def solution(n):

    ans = []
    visited = [0] * (n + 1)

    def back(level):
        if level == n:
            print(*ans)
            return
        
        for i in range(1, n + 1):
            if visited[i] != 0:
                continue

            visited[i] = 1
            ans.append(i)

            back(level + 1)

            visited[i] = 0
            ans.pop()

    back(0)

solution(n)