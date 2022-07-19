from collections import deque

# 리스트 메서드 사용 예제
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# 2
print(fruits.count('apple'))
# 0
print(fruits.count('tangerine'))
# 3
print(fruits.index('banana'))
# 6
print(fruits.index('banana', 4))

fruits.reverse()

# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
print(fruits)

fruits.sort()

# ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'pear']
print(fruits)

fruits.pop()

# ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange']
print(fruits)

# 리스트를 스택으로 사용하기
stack = [3, 4, 5]
stack.append(6)
stack.append(7)

# [3, 4, 5, 6, 7]
print(stack)

stack.pop()

# [3, 4, 5, 6]
print(stack)

stack.pop()
stack.pop()

# [3, 4]
print(stack)

# 리스트를 큐로 사용하기

queue = deque()