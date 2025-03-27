import random
from utils.questions import initial_questions
from game_state import GameState
from question_manager import QuestionManager
from quiz_actions import get_module_selection, get_num_questions, handle_quiz_session, get_next_action, get_explanations, save_scores, display_progress, display_graph

def display_menu():
    """Display the main menu options."""
    print("\n=== COSC Quiz Game Main Menu ===")
    print("1) Start New Quiz")
    print("2) Review Incorrect Questions Explanations")
    print("3) Practice Incorrect Questions")
    print("4) View Progress Graph")
    print("5) Exit Game")
    return input("\nEnter your choice (1-5): ")

def start_new_quiz(question_manager):
    """Handle the quiz session flow."""
    questions = question_manager.questions.copy()
    filtered_questions = get_module_selection(questions)
    num_questions = get_num_questions(len(filtered_questions))
    incorrect_questions, total_score = handle_quiz_session(filtered_questions, num_questions)
    save_scores(total_score, num_questions)
    return incorrect_questions

def main():
    game = GameState()
    question_manager = QuestionManager()
    incorrect_questions = []

    try:
        while game.running:
            print("\nWelcome to the Quiz Game!")
            print("Enter 'quit' at any time to exit.")
            choice = display_menu()

            if choice.lower() == 'quit':
                game.quit_game()

            if choice == '1':
                incorrect_questions = start_new_quiz(question_manager)
                input("\nPress Enter to return to main menu...")

            elif choice == '2':
                if incorrect_questions:
                    get_explanations(incorrect_questions)
                else:
                    print("\nNo incorrect questions to review.")
                input("\nPress Enter to return to main menu...")

            elif choice == '3':
                if incorrect_questions:
                    num_questions = get_num_questions(len(incorrect_questions))
                    new_incorrect, score = handle_quiz_session(incorrect_questions, num_questions)
                    incorrect_questions = new_incorrect
                else:
                    print("\nNo incorrect questions to practice.")
                input("\nPress Enter to return to main menu...")

            elif choice == '4':
                display_graph()
                input("\nPress Enter to return to main menu...")

            elif choice == '5':
                game.quit_game()
            
            else:
                print("\nInvalid choice. Please enter a number between 1 and 5.")

    except KeyboardInterrupt:
        print("\nQuiz interrupted. Exiting...")

    print("\nGreat study session!\nSee you next time.")

if __name__ == "__main__":
    main()

