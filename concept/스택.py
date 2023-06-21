# 재귀 함수
def recursive(data):
    if data<0:
        print("ended")
    else:
        print(data)
        recursive(data-1)
        print("returned", data)

# recursive(4)

# 1. recursive(4) : 4 / 11. returned 4
# 2. recursive(3) : 3 / 10. returned 3
# 3. recursive(2) : 2 / 9. returned 2
# 4. recursive(1) : 1 / 8. returned 1
# 5. recursive(0) : 0 / 7. returned 0
# 6. recursive(-1) :  ended

data_stack = list()

data_stack.append(1)
data_stack.append(2)

# print(data_stack)
# a = data_stack.pop()
# print(a, data_stack)

data_stack2 = list()

def push(data):
    data_stack2.append(data)

def pop():
    data = data_stack2[-1]
    del data_stack2[-1]
    return data

for idx in range(5):
    push(idx)

print(data_stack2)
pop()
print(data_stack2)

