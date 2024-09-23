from itertools import combinations_with_replacement
S, k = input().split()
S = sorted(S)
k = int(k)
for x in combinations_with_replacement(S, k):
    print(''.join(x))