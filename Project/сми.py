n = int(input())
arr = list(map(int, input().split()))
f = int(input())
queries = [list(map(int, input().split())) for _ in range(f)]

arr.sort()
k = 0
a = []
for b in range(len(arr)):
    for c in range(len(arr)):
        for query in queries:
            l, r = query
            if arr[b] >= l and arr[c] <= r:
                k = int(c) - int(b)
                k = int(k / 2)
    a.append(k)

print(*a)
