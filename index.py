import random
from utils.questions import initial_questions
from game_state import GameState
from question_manager import QuestionManager
from quiz_actions import get_module_selection, get_num_questions, handle_quiz_session, get_next_action, get_explanations


def main():
    game = GameState()
    question_manager = QuestionManager()
    questions = question_manager.questions.copy()

    try:
        while game.running:
            print("\nWelcome to the Quiz Game!")
            print("Enter 'quit' at any time to exit.")
            print(" ")

            filtered_questions = get_module_selection(questions)
            
            num_questions = get_num_questions(len(filtered_questions))
            incorrect_questions = handle_quiz_session(filtered_questions, num_questions)
            
            choice = get_next_action()
            if choice == '1':
                questions = question_manager.questions.copy()
            elif choice == '2':
                if incorrect_questions:
                    questions = incorrect_questions.copy()
                    get_explanations(questions)
                else:
                    print("There are no incorrect questions to review.")
                    continue
            else:  
                game.quit_game()

    except KeyboardInterrupt:
        print("\nQuiz interrupted. Exiting...")

    print("\nGreat study session!\nSee you next time.")

if __name__ == "__main__":
    main()

