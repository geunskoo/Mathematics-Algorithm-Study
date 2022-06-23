#입력
n = int(input())
step = [int(input()) for i in range(n)]

#처리(DP)

if n > 3:
    dp = [0] * (n+1)
    dp[0] = step[0]
    dp[1] = step[0] + step[1]
    dp[2] = max(step[0]+step[2],step[1]+step[2])
    
    for i in range(3,n):
        dp[i] = max((dp[i-2] + step[i]),dp[i-3] + step[i-1]+step[i])
    print(dp[n-1])
    
elif n == 1: print(step[0])
elif n == 2: print(step[0] + step[1])
else: print(max(step[0]+step[2],step[1]+step[2]))