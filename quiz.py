# Simple Quiz App

# List of questions, options, and answers
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["lahore", "Islamabad", "Karachi", "delhi"],
        "answer": "Islamabad"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "What is 7 x 6?",
        "options": ["42", "36", "48", "52"],
        "answer": "42"
    }
]
score = 0

# Quiz logic
for i, q in enumerate(questions):
    print(f"\nQuestion {i + 1}: {q['question']}")
    for idx, option in enumerate(q['options']):
        print(f"  {idx + 1}. {option}")
    
    try:
        choice = int(input("Your answer (1-4): "))
        if q['options'][choice - 1].lower() == q['answer'].lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is: {q['answer']}")
    except (ValueError, IndexError):
        print("❗ Invalid input. Skipped.")

print(f"\n🎉 Quiz finished! Your score: {score}/{len(questions)}")


