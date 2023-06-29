- **1859.** 백만 장자 프로젝트 230626
    
    ```python
    # 테스트 케이스
    T = int(input())
    
    for test_case in range(1, T + 1):
    	# 매매가 갯수
      total = int(input())
    	# 매매가 배열
      arr = list(map(int, input().split()))
    	# 마지막날 매매가를 maxProfit으로 초기화
      maxProfit = arr[-1]
    	# 이익
      profit = 0
      
     # 뒤에서 순회
      for i in range(total-2, -1, -1):
    		# maxProfit보다 작으면
        if maxProfit > arr[i]:
    			# 이익 계산 (maxPropfit - 현재가)
          profit += maxProfit - arr[i]
        else:
    			# maxProfit보다 큰경우 maxProfit을 현재가로 변경함
          maxProfit = arr[i]
    
      print('#{} {}'.format(test_case, profit))
    ```
    
- **2007.** 패턴 마디의 길이 230626
    
    ```python
    # 마디찾기
    # abcdabcdabcd
    # a == b?
    # ab == cd ?
    # abc == cda ?
    # abcd == abcd
    
    T = int(input())
        
    for test_case in range(1, T + 1):
      cnt = 0
      pattern = list(input())
      result = ''
      i = 0
      j = 1
      for idx in pattern:
    		# 마디를 하나씩 늘려가면서 문자열을 비교함
        str1 = pattern[i:j]
        str2 = pattern[j:j+j]
        if str1 != str2:
    			# 같지 않다면 마디 j를 1 증가함
          j += 1
        else:
    			# 같다면 result에 저장
          result = str1
    			
      print('#{} {}'.format(test_case, len(result)))
    ```

    <hr>

- **2005.** 파스칼의 삼각형 230629
    
    ```python
    // 1, 2 -> temp = [1], temp = [1,1]
    // 이후 index -> result = [1,1]이 기본이고
    // result에 뒤에서 두번째 값으로 temp[i] + temp[i+1] 값을 넣어줌
    // 3 -> [1, 2, 1] => 값이 추가된 리스트를 temp에 다시 넣음
    // 이것을 계속 반복함
    
    test = int(input())
    for TEST in range(1, test+1):
      T = int(input())
      print('#{}'.format(TEST))
      temp = [1]
      result = []
      for test_case in range(1, T + 1):
        if test_case == 1:
          result = [1]
        elif test_case == 2:
          temp.append(1)
        else:
          total = len(temp)
          result = [1,1]
          for i in range(0, total-1):
            result.insert(-1, temp[i] + temp[i+1])
          temp = result
              
        result = temp
        print(' '.join(list(map(str, result))))
    ```
    
- **1989.** 초심자의 회문 검사 2306629
    
    ```python
    # 문자열의 길이가 짝수이면
    # 문자열을 절반 잘라서 비교하기
    # test[:mid], test[mid:][::-1]
    
    # 파이썬에서 문자열 뒤집기 string[::-1]
    
    # 문자열의 길이가 홀수이면
    # 가운데 문자 빼고 절반 잘라서 비교하기
    # test[:mid-1], test[mid:][::-1]
    
    # 가운데 인덱스 값은 math.ceil(문자열 길이/2)
    import math
    
    T = int(input())
    for test_case in range(1, T + 1):
      result = 0
      test = str(input())
      mid = math.ceil(len(test)/2)
      if len(test) % 2 != 0 :
        str1 = test[:mid-1]
      else:
        str1 = test[:mid]
    
      str2 = test[mid:][::-1]
      
      if str1 == str2:
        result = 1
      
      print('#{} {}'.format(test_case, result))
    ```

    <hr>
