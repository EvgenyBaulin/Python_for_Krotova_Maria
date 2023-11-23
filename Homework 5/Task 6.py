def possible_numbers(n, questions):
	possible = set(range(1, n + 1))

	for i in range(0, len(questions), 2):
		question_set = set(map(int, questions[i].split()))
		answer = questions[i + 1]

		if answer == "YES":
			possible &= question_set
		else:
			possible -= question_set

	return sorted(possible)


n = int(input())
questions = []

while True:
	question = input()
	if question == "HELP":
		break
	questions.append(question)

possible = possible_numbers(n, questions)
print(*possible)
