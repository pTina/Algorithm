# https://www.acmicpc.net/problem/2920

# c d e f g a b C
# 1 2 3 4 5 6 7 8
# 1~8 순서대로 연주하면 ascending
# 8~1 역순으로 연주하면 descending
# 둘 다 아니면 mixed

# 연수한 순서가 주어졌을 때 ascending, descending, mixed 판별하는 프로그램을 작성하시오.


# 내가 푼 코드
arr = list(map(int, str(input()).split()))
temp = [0 for i in range(8)]

for i in range(len(arr)):
    if arr[i] == i+1:
        temp[i] = 't'
    elif arr[i] == 8-i:
        temp[i] = 'f'
    
cnt1 = temp.count('t')
cnt2 = temp.count('f')

if cnt1 == 8:
    print('ascending')
elif cnt2 == 8:
    print('descending')
else:
    print('mixed')

# 강의 풀의 코
'''
1. 리스트에서 원소를 차례대로 비교한다.
2. 비교할 때 두 원소를 기준으로 오름, 내림 여부 체크

'''

a = list(map(int, str(input()).split()))

ascending = True
descending = True

for i in range(1, 8):
    if a[i] > a[i-1]:
        descending = False
    elif a[i] < a[i-1]:
        ascending = False
    
if ascending:
    print('ascending');
elif descending:
    print('descending')
else:
    print('mixed')






