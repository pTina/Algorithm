# acmicpc.net/problem/11650

# x가 증가하는 순
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬
# 좌표: 정수, 위치가 같은 두 점은 없다.

# 파이썬 기본 정렬 라이브러리: 튜플의 인덱스 순서대로 오름차순 정렬
# => 기본적으로 x가 같으면 y순으로 정렬함

n = int(input())
arr = []

for i in range(n):
    x, y = map(int, input().split(' '))
    arr.append((x, y))

arr = sorted(arr)

for a in arr:
    print(a[0], a[1])