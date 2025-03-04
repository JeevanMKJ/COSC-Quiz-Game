import random
from questions import initial_questions
from quiz_actions import get_module_selection, get_num_questions, handle_quiz_session, get_next_action

def main():
    questions = initial_questions.copy()
    exit_game = False

    while not exit_game:
        
        filtered_questions = get_module_selection(questions)
        
        num_questions = get_num_questions(len(filtered_questions))
        incorrect_questions = handle_quiz_session(filtered_questions, num_questions)
        
        choice = get_next_action()
        if choice == '1':
            questions = initial_questions.copy()
        elif choice == '2':
            if incorrect_questions:
                questions = incorrect_questions.copy()
            else:
                print("There are no incorrect questions to review.")
                continue
        else:  
            exit_game = True

    print("\nGreat study session!\nSee you next time.")

if __name__ == "__main__":
    main()

