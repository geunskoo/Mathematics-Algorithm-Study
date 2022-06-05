import time
import random
# 0 ~ 10000 정수, 10000개 생성
num = [random.randint(0,10001) for i in range(10000)]
num1 = num.copy()
num2 = num.copy()
num3 = num.copy()
num4 = num.copy()
num5 = num.copy()
test = []
###########################################################
#선택 정렬
###########################################################
start = time.time()
for i in range(len(num)):
    min_index = i
    for j in range(i+1,len(num)):
        if num[min_index] > num[j]:
            min_index = j

    num[i],num[min_index] = num[min_index],num[i]

end = time.time()
test.append(end - start)
###########################################################
#삽입 정렬
###########################################################
start = time.time()
for i in range(1,len(num1)):
    for j in range(i,0,-1):
        if num1[j] < num1[j-1]:
            num1[j],num1[j-1] = num1[j-1],num1[j]
        else:
            break
end = time.time()
test.append(end - start)
###########################################################
#버블 정렬
###########################################################
start = time.time()
for i in range(len(num2)-1):
    for j in range(len(num2)-1-i):
        if num2[j] < num2[j+1]:
            num2[j],num2[j+1] = num2[j+1],num2[j]
end = time.time()
test.append(end - start)


###########################################################
#계수 정렬
###########################################################
start = time.time()
counter = [0]*(max(num3) + 1)

for i in num3:
    counter[i] += 1
for i in range(max(num3)+1):
    if counter[i] != 0:
        for _ in range(counter[i]):
            print('')
end = time.time()           
test.append(end - start)

############################################################
#퀵 정렬
###########################################################
start = time.time()
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start #피벗 초기값은 첫번째 요소
    left = start+1
    right = end
    
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left+=1
            
            #피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right-=1
            
        if left>right: # 엇갈렸다면 작은 right -=1 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
            
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체 
            array[left], array[right] = array[right], array[left]
            
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
    
quick_sort(num4, 0, len(num4)-1)

end = time.time()           
test.append(end - start)

############################################################
############################################################
start = time.time()
num5 = num5.sort()
end = time.time()           
test.append(end - start)
sort = ['선택 정렬','삽입 정렬','버블 정렬','계수 정렬','퀵    정렬','내장 함수']
print(len(num),'개의 random 정수 생성')
for i in range(len(test)):
    print(f'{sort[i]} : {test[i]:.10f} 초')