n = int(input())

for _ in range(n):
    m = input()
    try:
        if m == "0":
            print(False)
            continue
        result = float(m)
        print(True)
    except ValueError:
        print(False)
               
