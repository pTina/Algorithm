# https://www.acmicpc.net/problem/10989

# 1 ≤ N(데이터의 수) ≤ 10,000,000
# 주어지는 수: 10,000 보다 작거나 같음

# 정렬 알고리즘: 시간복잡도 nlog(n)
# 데이터 갯수 1000만 => 파이썬의 기본 정렬 알고리즘으로 풀 수 없음
# 데이터의 수는 많지만, 데이터의 범위는 좁다. 

# 시간복잡도 O(N) 정렬 알고리즘을 사용해야 한다.
# 수의 범위가 1 ~ 10,000 이므로 계수 정렬 이용할 수 있다.
# 계수 정렬: 수 범위 제한적일 때 사용할 수 있다. 훨씬 빠르다.

# 데이터의 갯수가 많을 때는 
# input() 함수보다 빠른 sys.stdin.radline()을 사용해야 한다.

import sys

n = int(sys.stdin.readline())
arr = [0]*10001

for i in range(n):
    num = int(sys.stdin.readline())
    arr[num] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)