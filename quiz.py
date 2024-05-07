URLS = "URLS"
QUESTIONS = "Questions"

Quizzes = {
    "bbc.com": {
        "What's the score?": {"options": ["1-0", "2-0", "3-1", "4-0"], "answer": 3},
        "What is this rabbit?": {"options": ["Cute one", "Small one", "Short one", "Thin one"], "answer": 0}
    },
    "google.com": {
        "How many letters in this?": {"options": ["2", "3", "6", "8"], "answer": 2},
        "How many fun?": {"options": ["45", "56", "2", "88"], "answer": 3}
    }
}


for site, questions in Quizzes.items():
    print(f"Site: {site}")
    for question, details in questions.items():
        print(f"Question: {question}")
        for i, option in enumerate(details["options"]):
            print(f"{i}: {option}")
        
        # User input to choose an option
        user_answer = int(input("Enter the option number: "))
        user_answer -= 1
        
        # Check if the user's answer is correct
        if user_answer == details["answer"]:
            print("Correct!")
        else:
            print("Incorrect!")
        print()  # Separate each question
