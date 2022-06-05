import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int,input().split()))
m = int(input())
fi_card = list(map(int,input().split()))

dict = {}
for i in card:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1

for i in fi_card:
    if i in dict.keys():
        print(dict[i],end=' ')
    else:
        print(0,end=' ')