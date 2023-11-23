def read_dictionary(n):
	dictionary = {}

	for _ in range(n):
		word = input().strip()

		if word.lower() in dictionary:
			for i in range(len(word)):
				if word[i].isupper():
					dictionary[word.lower()].append(i)
		else:
			for i in range(len(word)):
				if word[i].isupper():
					dictionary[word.lower()] = [i]

	return dictionary


def count_errors(dictionary, exercise):
	errors = 0
	words = exercise.split()

	for word in words:
		boo = False

		for i in range(len(word)):
			if word[i].isupper():
				boo += 1

		if boo != 1:
			errors += 1
			continue

		word_lower = word.lower()

		if word_lower in dictionary:
			for i in range(len(word)):
				if word[i].isupper():
					accents = i
			if accents not in dictionary[word_lower]:
				errors += 1

	return errors


n = int(input())
accent_dictionary = read_dictionary(n)
exercise_text = input()

result = count_errors(accent_dictionary, exercise_text)
print(result)
