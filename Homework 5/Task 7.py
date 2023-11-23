def august_cheating(n, questions):
	possible = set(range(1, n + 1))

	for question in questions:
		question_set = set(map(int, question.split()))

		if len(possible & question_set) <= (len(possible) // 2):
			answer = "NO"
		else:
			answer = "YES"

		print(answer)

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

answer = august_cheating(n, questions)
print(*answer)
