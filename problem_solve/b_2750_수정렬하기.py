
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 1. 선택 정렬 알고리즘
#       첫 번째 데이터를 두 번째 데이터 ~ 마지막 데이터와 비교
#       가장 작은 값 또는 큰 값을 맨 앞쪽으로 보내는 방법

n = int(input())
arr = list()

for i in range(n):
    data = int(input())
    arr.append(data)

arr.sort()

for i in range(n):
    print(arr[i])