#2805 나무자르기 / 실버 2

n,m = map(int,input().split())
trees = list(map(int,input().split()))

up = max(trees)
down = 0

while down <= up:
    sum = 0
    cut = (up + down) // 2

    # 나무를 자르고 얻은 길이 - > sum
    for tree in trees:
        if tree - cut > 0:
            sum += tree - cut
    
    # 조건을 만족하는 cut을 ans에 저장.
    # 최대높이의 cut을 ans에 갱신 해줌.
    if sum >= m:
        down = cut + 1
        ans = cut
    else:
        up = cut - 1
print(ans)
