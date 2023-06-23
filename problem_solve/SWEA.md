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
