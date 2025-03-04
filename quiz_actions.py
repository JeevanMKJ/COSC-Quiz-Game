import random

def get_module_selection(questions):
    """Get the module selection from the user and return filtered questions."""

    modules = sorted(list(set(q['module'] for q in questions)))
    
    while True:
        print("\nWhich module would you like to be tested on?")
        print("0) All modules")
        for module in modules:
            print(f"{module}) Module {module}")
        
        choice = input(f"\nEnter module number (0-{max(modules)}): ")
        
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                return questions 
            elif choice in modules:
               
                return [q for q in questions if q['module'] == choice]
            
        print(f"\nERROR: Please enter a number between 0 and {max(modules)}")

def get_num_questions(total_questions):
    """Get the number of questions the user wants to answer."""
    while True:
        num_questions_input = input(f"How many questions do you want (max {total_questions}): ")
        if num_questions_input.isdigit():
            num_questions = int(num_questions_input)
            if 1 <= num_questions <= total_questions:
                return num_questions
            print(f"ERROR\nPlease enter a number between 1 and {total_questions}")
        else:
            print(f"ERROR\nPlease enter a valid number.")

def ask_question(question_data, question_num):
    """Ask a single question and return whether it was answered correctly."""
    print(f"Question {question_num}: {question_data['question']}")
    for option in question_data['options']:
        print(option)

    user_answer = input("Enter answer (a, b, c or d): ")
    is_correct = user_answer == question_data['answer']
    
    if is_correct:
        print("Correct Answer!\n")
    else:
        print(f"Wrong! The correct answer is {question_data['answer']}.\n")
    
    return is_correct

def handle_quiz_session(questions, num_questions):
    """Run a quiz session and return the score and incorrect questions."""
    random.shuffle(questions)
    total_score = 0
    incorrect_questions = []

    for i in range(num_questions):
        question_data = questions[i]
        if ask_question(question_data, i + 1):
            total_score += 1
        else:
            incorrect_questions.append(question_data)

    print(f"Your total score is: {total_score}/{num_questions}")
    return incorrect_questions

def get_next_action():
    """Get the user's choice for the next action."""
    while True:
        print("\nWhat do you want to do next?")
        print("1) Play again with new questions?")
        print("2) Go through the questions that were answered wrong?")
        print("3) Exit the game?")
        choice = input("Enter (1, 2 or 3): ")
        
        if choice in ['1', '2', '3']:
            return choice
        print("\nInvalid choice. Enter either 1, 2 or 3.")

