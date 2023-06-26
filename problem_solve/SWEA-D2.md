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
