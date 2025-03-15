# Favourite Singer 
from collections import Counter
n = int(input())
a = list(map(int, input().split()))[:n]
c = Counter(a)
maxi = max(c.values())
print(list(c.values()).count(maxi))