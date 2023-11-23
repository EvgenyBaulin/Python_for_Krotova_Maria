words = {}
with open("input.txt") as f:
	for line in f:
		b = line.split()
		for word in b:
			word = word.strip()
			if word in words:
				print(words[word], end = ' ')
				words[word] += 1
			else:
				print(0, end = ' ')
				words[word] = 1
