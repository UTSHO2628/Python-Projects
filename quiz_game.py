def quiz_game():
    questions = {
        "What is the capital of France?": "Paris",
        "What is 22 + 8?": "30",

         "What is the capital of Spain?": "Madrid",
        "What is the color of the sky?": "Blue",
        "What is the capital of Italy?": "Rome"
    }
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            score += 1
            print("Correct!")
        else:
            print("Wrong! The correct answer is", answer)
    print(f"Your final score is {score}/{len(questions)}")
quiz_game()