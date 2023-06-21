# https://www.acmicpc.net/problem/10814

# 나이가 증가하는 순
# 나이가 같으면 먼저 가입한 사람이 앞
# 나이 이름
# 1 <= 나이 <= 200
# 이름: 알파벳 대소문자 <= 100
# 가입한 순으로 한 줄에 한 명씩 입력됨



n = int(input())
arr = list()

for i in range(n):
    user = input().split(' ')
    arr.append([int(user[0]), user[1]])

# x[0] 첫 번째 원소를 기준으로 정렬함
# 나머지 원소에 대해서는 stable한 성격을 지님
# stable: 앞에 있던 원소가 정렬된 이후에도 앞에 들어가도록 됨
arr = sorted(arr, key=lambda x: x[0])

for a in arr:
    print(a[0], a[1])
    

        