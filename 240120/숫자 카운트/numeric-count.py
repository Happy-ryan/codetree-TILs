N = int(input())
predicts = [list(map(int, input().split())) for _ in range(N)]
# 서로다른 세자리..100 ~ 999 밖에 없음...
# 전수조사 쌉가능하다..
# 10개 질문 * 1000개의 숫자 * 3자리 > 완탐 충분히 가능!

def check(candidate_number: int, predict: list[int]):
    candidate = []
    pre = []
    for i in range(1, 4):
        a = candidate_number % (10 ** i) // (10 ** (i - 1))
        p = predict[0] % (10 ** i) // (10 ** (i - 1))

        if a in candidate or a == 0:
            return False
        candidate.append(a)

        if p in pre or p == 0:
            return False
        pre.append(p)


    cnt_1 = 0
    cnt_2 = 0

    for a, p in zip(candidate, pre):
        if a == p:
            cnt_1 += 1
        else:
            if p in candidate:
                cnt_2 += 1

    if cnt_1 == predict[1] and cnt_2 == predict[2]:
        return True
    return False


cnt = set(range(100, 1000))
for predict in predicts:
    candidate_list = set()
    for candidate_number in range(100, 1000):
        if check(candidate_number, predict):
            candidate_list.add(candidate_number)   
    # 각 질문에 대해서 교집합으로 만족하는 것만 남기기     
    cnt = cnt & candidate_list


print(len(cnt))

# 틀린이유1.
# 각 질문들이 필터 역할을 해야함, 지금처럼 한 질문에 대해서 100 ~ 1000 전수조사를 때리면 각 질문에 대해서는 만족하는 후보값이
# 얻어지겠지만 모두 만족하는 값이 되는건 아니다.
# 질문들 모두 만족해야함!

# 틀린이유2.
# 서로다른 숫자! 때문에 틀린듯!
# 0도 안포함됨. 서로다른 1~9!