#14499 주사위 굴리기
1231231
#주사위 데이터 1,1이 아랫면
dice_col = [0,0,0]
dice_row = [0,0,0,0]

#이동 동(0) 서(1) 북(2) 남(3)
dx = [0,0,-1,1]
dy = [1,-1,0,0]

#동(1)서(2)북(3)남(4)
def throw_dice(d):
    global dice_col
    global dice_row
    if d == 4: 
        dice_row = dice_row[1:] + [dice_row[0]]
        dice_col[1] = dice_row[1]
    elif d == 3: 
        dice_row = [dice_row[-1]] + dice_row[:-1]
        dice_col[1] = dice_row[1]
    elif d == 2:
        temp = dice_col[-1]
        dice_col = [dice_row[-1]]+ dice_col[:-1]
        dice_row[-1] = temp
    elif d == 1:
        temp = dice_col[0]
        dice_col = dice_col[1:] + [dice_row[-1]]
        dice_row[-1] = temp

   


#입력
n,m,x,y,cnt = map(int,input().split())
game = [list(map(int,input().split())) for _ in range(n)]
cmds = list(map(int,input().split()))

#주사위 굴리고, 숫자 복사 구현부
for cmd in cmds:
    nx = x + dx[cmd - 1]
    ny = y + dy[cmd - 1]

    if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
        continue

    throw_dice(cmd)

    if game[nx][ny] == 0:
        game[nx][ny] = dice_row[1]
    else:
        dice_col[1] = game[nx][ny]
        dice_row[1] = game[nx][ny]
        game[nx][ny] = 0

    print(dice_row[-1],dice_row[1])

    x, y = nx, ny