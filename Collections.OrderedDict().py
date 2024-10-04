from collections import OrderedDict

N = int(input())
dict1 = OrderedDict()
for x in range(N):
    item, price = input().rsplit(' ', 1)
    dict1[item]= dict1.get(item, 0)+ int(price)
    
for item, price in dict1.items():
    print(f"{item} {price}")
