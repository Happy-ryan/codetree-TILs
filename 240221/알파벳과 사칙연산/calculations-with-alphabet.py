# from collections import defaultdict

# def find_cmd_and_number_count(s: str):
#     cmd_list, al_list = [], []
#     for x in s:
#         if x in "+-*":
#             cmd_list.append(x)
#         else:
#             al_list.append(x)

#     return cmd_list, al_list


# def calculate(cmd_list, al_list, number_dic):
#     tmp = number_dic[al_list[0]]
#     for cmd, number in zip(cmd_list, al_list[1:]):
#         if cmd == "+":
#             tmp += number_dic[number]
#         elif cmd == "-":
#             tmp -= number_dic[number]
#         elif cmd == "*":
#             tmp *= number_dic[number]
#     return tmp


# def assign_alphabet_number(al_list, ans):
#     number_dic = defaultdict()
#     al_list = list(set(al_list))
#     al_list.sort()
#     for al, num in zip(al_list, ans):
#         number_dic[al] = num

#     return number_dic



# max_val = -2**(31)

# def solution(s: str):
#     cmd_list, al_list = find_cmd_and_number_count(s)

#     k = len(set(al_list))

#     ans = []
#     def dfs(level):
#         global max_val
#         if level == k:
#             number_dic = assign_alphabet_number(al_list, ans)
#             max_val = max(max_val, calculate(cmd_list, al_list, number_dic))
#             return
#         for i in range(1, 5):
#             ans.append(i)
#             dfs(level + 1)
#             ans.pop()
    
#     dfs(0)
#     print(max_val)
#     return

# s = input()
# solution(s)

# # 틀린이유1: 같은 알파벳에 대해서는 같은 값이 들어가야한다!
# # k개 중 하나를 n번 선택하는 백트래킹 유행 -> 모든 조합(순얄)을 만들어서 전수조사하는 것!
# # ans를 구하는데 특별한 조건이 있지 않음.

# a ~ f에 수를 배정해야함!
# 중복 알파벳에 주의하자!
# k는 알파벳의 종류
def dfs(level, k):
    global ans
    if level == k:
        dic = assign(assignment, alpabet)
        ans = max(ans, calculate(dic))
        return
    
    for num in range(1, 5):
        assignment.append(num)
        dfs(level + 1, k)
        assignment.pop()
        
# 인덱스 매칭!
def assign(assignment, alpabet):
    al = list(set(alpabet))
    al.sort()
    
    dic = {}
    for alpabet, num in zip(al, assignment):
        dic[alpabet] = num

    return dic

def calculate(dic):
    tmp = 0
    for idx in range(len(cmds)):
        if cmds[idx] == '+':
            tmp += dic[alpabet[idx]]
        elif cmds[idx] == '-':
            tmp -= dic[alpabet[idx]]
        elif cmds[idx] == '*':
            tmp *= dic[alpabet[idx]]
    return tmp


s = input()
ans = -2**(31)
alpabet = []
cmds = ["+"]
assignment = []

for x in s:
    if x not in  '+-*':
        alpabet.append(x)
    else:
        cmds.append(x)
        
k = len(set(alpabet))
dfs(0, k)
print(ans)