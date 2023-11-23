n = int(input())
marks = {}
for _ in range(n):
	line = input().split()
	marks[line[0]] = int(line[1])

marks = sorted(marks.items(), key = lambda item: item[1], reverse = True)

for i in marks:
	print(i[0])
