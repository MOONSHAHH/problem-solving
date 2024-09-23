N, M = map(int, input().split())
n = ".|."
m = "-"

for i in range(N):
    if i < (N-1)/2:
        print((n*(i*2)+n).center(M, m))
    elif i == (N-1)/2:
        print("WELCOME".center(M, m))
    else:
        print((n*(((N-i)-1)*2)+n).center(M, m))
