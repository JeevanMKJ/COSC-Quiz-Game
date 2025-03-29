import random
import matplotlib.pyplot as plt
from game_state import GameState

game = GameState()

def get_module_selection(questions):
    """Get the module selection from the user and return filtered questions."""

    modules = sorted(list(set(q['module'] for q in questions)))
    
    while True:
        print("\nWhich module would you like to be tested on?")
        print("0) All modules")
        for module in modules:
            print(f"{module}) Module {module}")
        
        choice = input(f"\nEnter module number (0-{max(modules)}): ")

        if choice.lower() == 'quit':
            game.quit_game()
        
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

        if num_questions_input.lower() == 'quit':
            game.quit_game()    

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

    if user_answer.lower() == 'quit':
        game.quit_game()

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
    return incorrect_questions, total_score


def get_next_action():
    """Get the user's choice for the next action."""
    while True:
        print("\nWhat would you like to do next?")
        print("1) Start New Quiz")
        print("2) Review Incorrect Questions Explanations")
        print("3) Practice Incorrect Questions")
        print("4) View Progress Graph")
        print("5) Exit Game")
        choice = input("Enter (1-5): ")

        if choice.lower() == 'quit':
            game.quit_game()

        if choice in ['1', '2', '3', '4', '5']:
            return choice
        print("\nInvalid choice. Please enter a number between 1 and 5.")


def get_explanations(questions):
    """Display explanations for incorrectly answered questions."""
    print("\n=== Explanations for Incorrect Answers ===")
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question['question']}")
        print("\nCorrect Answer:", end=" ")
        for option in question['options']:
            if option.startswith(f"{question['answer']}."):
                print(option)
                break
        print(f"\nExplanation: {question['explanation']}")
        print("\n" + "-"*50)


def save_scores(total_score, num_questions):

    with open('scores.txt', 'a') as scores_file:
        scores_file.write(f"{str(total_score)}\n")
        scores_file.write(f"{str(num_questions)}\n")


def display_progress():
    try:
        scores_list = []
        with open('scores.txt', 'r') as read_scores_file:
            file_score = read_scores_file.readline()

            while file_score != '':
                file_question = read_scores_file.readline()

                file_score = file_score.strip('\n')
                file_question = file_question.strip('\n')

                session_score = int(file_score) / int(file_question)
                scores_list.append(session_score)

                file_score = read_scores_file.readline()

    except FileNotFoundError:
        print("No scores found. Please take a quiz first.")
        return []

    return scores_list
    

def display_graph():
    try:
        score_list = display_progress()
        quiz_attempt = []

        for i in range(1, len(score_list) + 1):
            quiz_attempt.append(i)

        x_coords = quiz_attempt
        y_coords = score_list

        plt.xlim(xmin = 1, xmax = len(score_list) + 1)
        plt.ylim(ymin = 0, ymax = 1.5)

        plt.plot(x_coords, y_coords)

        plt.xlabel('Quiz Attempt')
        plt.ylabel('Score (%)')
        plt.title('Quiz Score Progress')
        plt.grid(True)

        plt.show()
    
    except Exception as e:
        print(f"Error displaying graph: No scores found. \nDetails: {e}")

