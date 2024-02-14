numbers = list(map(int, input().split()))
min_odd = min(filter(lambda x: x % 2 != 0, numbers))
print(min_odd)
