# https://www.acmicpc.net/problem/1427

# 강의 풀이
# 1) 자릿수 기준 정렬이므로 9~0까지 차례대로 확인
# 2) 각 숫자에 대하여 해당 숫자의 개수 계산하여 출력
# ex. 988297
# 9: 2개 -> 99
# 8: 2개 -> 9988
# 7: 1개 -> 99887
# 6: 0개
# 5: 0개
# 4: 0개
# 3: 0개
# 2: 1개 -> 99882
# 1: 0개
# 0: 0개
# 출력: 99882

arr2 = input()

for i in range(9, -1, -1):
    for j in arr2:
        if int(j) == i:
            print(i, end='')


# 내가 품
arr = list(map(int, list(input())))

arr.sort(reverse=True)
reuslt = ''.join(list(map(str, arr)))
print(reuslt)
