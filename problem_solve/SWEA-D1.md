- **2072.** 홀수만 더하기 230612
    
    ```python
    T = int(input())
    cnt = 0
    for test_case in range(1, T + 1):
        test_case = list(map(int, input().split(' ')))
        arr1 = [x for x in test_case if x % 2 == 0]
        cnt += 1
        result = sum(arr1)
        print('#{} {}'.format(cnt, result))
    ```
    
- **2071.** 평균값 구하기 230613
    
    ```python
    T = int(input())
    cnt = 0
    for test_case in range(1, T + 1):
      test_case = list(map(int, input().split(' ')))
      avg = round(sum(test_case) / len(test_case))
      cnt += 1
      print('#{} {}'.format(cnt, avg))
    ```
    
- **2070.** 큰 놈, 작은 놈, 같은 놈 230613
    
    ```python
    T = int(input())
    
    for test_case in range(1, T + 1):
      a, b = list(map(int, input().split(' ')))
      
      if a == b:
        result = '='
      elif a > b:
        result = '>'
      else:
        result = '<'
        
      
      print('#{} {}'.format(test_case, result))
    ```
    
- **2068.** 최대수 구하기 230613
    
    ```python
    T = int(input())
    
    for test_case in range(1, T + 1):
      arr1 = list(map(int, input().split(' ')))
      result = arr1[0]
      for x in range(1, len(arr1)):
        if arr1[x] > result: result = arr1[x]
      
      print('#{} {}'.format(test_case, result))
    ```
    

---

- **2063.** 중간값 찾기 230614
    
    ```jsx
    import math
    
    T = int(input())
    
    arr1 = list(map(int, input().split(' ')))
    arr1.sort()
    print(arr1[math.floor(T/2)])
    ```
    
- **2058.** 자릿수 더하기 230614
    
    ```jsx
    T = input()
    
    result = list(map(int, str(T)))
    print(sum(result))
    ```
    
- **2056.** 연월일 달력 230614
    
    ```jsx
    mDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    T = int(input())
    for test_case in range(1, T + 1):
      str1 = str(input())
      year = str1[0:4]
      month = str1[4:6]
      day = str1[-2:]
    
      date = '{}/{}/{}'.format(year,month, day) if 12-int(month) > 0 and month != '00' and int(month) <= 12 and int(day) <= mDay[int(month)-1] else -1
      
      print('#{} {}'.format(test_case, date))
    ```
    
- **2050.** 알파벳을 숫자로 변환 230614
    
    ```python
    from string import ascii_lowercase
    
    alpha_dic = {string: i for i, string in enumerate(ascii_lowercase, start=1)}
    
    T = str(input()).lower()
    
    result = ''
    for alpha in T:
      result += " {}".format(alpha_dic[alpha])
    print(result.strip())
    ```
    

---

- **2043.** 서랍의 비밀번호 230615
    
    ```python
    P, K = list(map(int, input().split(' ')))
    
    max = 999
    result = 1
    if K <= P:
        result +=(P-K)
    else:
        result += (999-K)+P
    
    print(result)
    ```
    
- **2027.** 대각선 출력하기 230615
    
    ```python
    for i in range(5):
      str1 = list('++++')
      str1.insert(i, '#')
      print(''.join(str1))
    
    """
    출력 결과
    
    #++++
    +#+++
    ++#++
    +++#+
    ++++#
    
    """
    ```
    
- **2025.** N줄덧셈 230615
    
    ```python
    T = int(input())
    
    arr1 = [i+1 for i in range(T)]
    print(sum(arr1))
    ```
    
- **2019.** 더블더블 230615
    
    ```python
    T = int(input())
    temp = 1
    result = '1'
    for i in range(1, T+1):
      temp = temp*2
      result += ' {}'.format(temp)
    print(result)
    ```
    
- **1936.** 1대1 가위바위보 230615
    
    ```python
    가위: 1, 바위: 2, 보: 3
    [A가 가위일 때(1) 이기기 위해 B가 내야할 것(3),
    A가 바위일 때(2) 이기기 위해 B가 내야할 것(1),
    A가 보일 때(3) 이기기 위해 B가 내야할 것(2)]
    game = [3, 1, 2]
    
    A, B = map(int, input().split())
    result = 'A' if B == game[A-1] else 'B'
    
    print(result)
    ```

<hr>

- **1933.** 간단한 N 의 약수 230623
    
    ```python
    T = int(input())
    result = []
    for test_case in range(1, T + 1):
      if T % test_case == 0:
        result.append(test_case)
    
    print(' '.join(str(s) for s in result))
    # 이것과 같음
    # ' '.join(list(map(str, result)))
    ```
    
- **1926.** 간단한 369게임 230623
    
    ```python
    T = int(input())
    
    result = []
    
        
    for test_case in range(1, T + 1):
      if test_case < 10:
        if test_case == 3 or test_case == 6 or test_case == 9:
          result.append('-')
        else:
          result.append(str(test_case))
      else:
        temp = list(str(test_case))
        cnt = 0
        for i in temp:
          if i == '3' or i == '6' or i == '9':
            cnt+=1
    
        if cnt > 0:
          result.append('-'*cnt)
        else:
          result.append(str(test_case))
    
    print(' '.join(result))
    ```
