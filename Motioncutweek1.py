# Step 1: Define Quiz Data
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A: Paris", "B: London", "C: Berlin", "D: Madrid"],
        "answer": "A"
    },
    {
        "question": "Which language is primarily spoken in Brazil?",
        "options": ["A: English", "B: Portuguese", "C: Spanish", "D: French"],
        "answer": "B"
    },
    {
        "question": "What is the smallest planet in our solar system?",
        "options": ["A: Earth", "B: Mars", "C: Mercury", "D: Venus"],
        "answer": "C"
    }
]

# Step 2: Implement the Quiz Logic
def ask_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    user_answer = input("Enter your answer (A, B, C, D): ").strip().upper()
    return user_answer

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False

def run_quiz(quiz_data):
    score = 0
    for question in quiz_data:
        user_answer = ask_question(question)
        if check_answer(user_answer, question["answer"]):
            score += 1
    print(f"Your final score is {score}/{len(quiz_data)}.")

# Step 3: User Interaction & Step 4: Scoring System
# Already integrated within the `run_quiz` function.

# Step 5: Customization
# Users can easily customize the quiz by modifying the `quiz_data` list.

# Running the quiz
run_quiz(quiz_data)
