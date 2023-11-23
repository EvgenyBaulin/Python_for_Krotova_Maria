words = {}
count = 0
with open("input.txt") as f:
	for line in f:
		line = line.strip()
		count += 1
		if line in words:
			words[line] += 1
		else:
			words[line] = 1

words_s = sorted(words.items(), key = lambda item: item[1], reverse = True)

print(words_s[0][0])
if words_s[0][1] <= count / 2:
	print(words_s[1][0])
