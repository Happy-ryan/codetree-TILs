# 보석을 쪼갤 수 없음, 담거나 담지 않거나만 선택할 수 있는 유형 0/1 냅색
# 보색을 쪼갤 수 있으면 fractional 냅색...무게 대비 가격이 높은 보석이 1순위가 된다!!
n, m = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(n)]

infos.sort(key=lambda x: -(x[1] // x[0]))


sum_val= 0
for weight, value in infos:
    if m >= weight:
        sum_val+= value
        m -= weight
    else:
        sum_val+= m * (value / weight)
        break
            
print(f"{sum_val:.3f}")