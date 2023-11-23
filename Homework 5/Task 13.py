n = int(input())
dict1 = {}
dict = {}

for _ in range(n):
	a, b = input().split()
	a.strip()
	b.strip()
	for a in dict1:
		dict1[a] = b
	for b in dict:
		dict[b] = a
n = input().strip()
if n in dict1:
	print(dict[n])
if n in dict1:
	print(dict1[n])
