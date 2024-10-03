from collections import deque

n = int(input())

de = deque()

for _ in range(n):
    operation = input().split(maxsplit=1)
    opp = operation[0]
    
    if opp == 'append':
        de.append(operation[1])
    elif opp == 'pop':
        de.pop()
    elif opp == 'popleft':
        de.popleft()
    elif opp == 'appendleft':
        de.appendleft(operation[1])

# Print the resulting deque if needed
print(de)