# 숫자의 범위 -10^9 ~ 10^9
# 아주 큰 숫자를 Array의 Index로 사용하기!!
# 숫자 범위와 무관하게 n개의 숫자에 대한 메모리만 사용!!

# n개의 숫자로 이루어진 수열 정보 하나
# m번에 걸쳐 특정 숫자가 주어지면 해당 숫자가 수열메 몇 개 있는지를 출력

n, m = map(int, input().split())
nums = list(map(int, input().split()))
wants = list(map(int, input().split()))

def solution(n, m, nums, wants):
    answer = ''
    # 리스트로 단순하게 count를 사용한다고 생각해보자!!
    # wants 에서 100,000
    # count 에서 100,000이므로 반드시 시간초과 발생한다!
    # for want in wants:
    #     print(nums.count(want))
    # dic을 활용해서 시간초과 방지하자!
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1

    for want in wants:
        if want in dic:
            answer += str(dic[want]) + ' '
        else:
            answer += '0 '

    return answer

print(solution(n, m, nums, wants))