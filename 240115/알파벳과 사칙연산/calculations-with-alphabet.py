def find_cmd_and_number_count(s: str):
    cmd_list, number_list = [], []
    for x in s:
        if x in "+-*":
            cmd_list.append(x)
        else:
            number_list.append(x)
    return cmd_list, number_list


def calculate(cmd_list, number_list):
    tmp = number_list[0]
    for cmd, number in zip(cmd_list, number_list[1:]):
        if cmd == "+":
            tmp += number
        elif cmd == "-":
            tmp -= number
        elif cmd == "*":
            tmp *= number
    return tmp


def solution(s: str):
    cmd_list, number_list = find_cmd_and_number_count(s)

    ans = []
    max_val = -2**(31)
    def dfs(level):
        #nolocal이 뭐야?
        nonlocal max_val
        if level == len(number_list):
            max_val = max(max_val, calculate(cmd_list, ans))
            return
        for i in range(1, 5):
            ans.append(i)
            dfs(level + 1)
            ans.pop()
    
    dfs(0)
    print(max_val)
    return

s = input()
solution(s)