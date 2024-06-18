def interactive_quiz():
    questions = [
        ("What is the capital of France?", "Paris"),
        ("What is 2 + 2?", "4"),
        # Add more questions here
    ]
    score = 0
    for question, correct_answer in questions:
        user_answer = input(question + " ")
        if user_answer.lower() == correct_answer.lower():
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
    print(f"Your final score is {score}/{len(questions)}")

interactive_quiz()