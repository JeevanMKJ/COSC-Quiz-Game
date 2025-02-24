import random
from questions import initial_questions


def main():
    questions = initial_questions.copy()
    exit_game = False

    while not exit_game:
        num_questions_input = input(f"How many questions do you want (max {len(questions)}): ")
        if num_questions_input.isdigit():
            num_questions = int(num_questions_input)
            if 1 <= num_questions <= len(questions):
                pass
            else:
                print(f"ERROR\nPlease enter a number between 1 and {len(questions)}")
                continue
        else:
            print(f"ERROR\nPlease enter a valid number.")
            continue

        random.shuffle(questions)

        total_score = 0
        incorrect_questions = []

        for i in range(num_questions):
            question_data = questions[i]
            print(f"Question {i + 1}: {question_data['question']}")
            for option in question_data['options']:
                print(option)

            user_answer = input("Enter answer (a, b, c or d): ")

            if user_answer == question_data['answer']:
                print("Correct Answer!\n")
                total_score += 1
            else:
                print(f"Wrong! The correct answer is {question_data['answer']}.\n")
                incorrect_questions.append(question_data)

        print(f"Your total score is: {total_score}/{num_questions}")

        while True:
            print("\nWhat do you want to do next?")
            print("1) Play again with new questions?")
            print("2) Go through the questions that were answered wrong?")
            print("3) Exit the game?")
            choice = input("Enter (1, 2 or 3): ")

            if choice == '1':
                questions = initial_questions.copy()
                break
            elif choice == '2':
                if incorrect_questions:
                    questions = incorrect_questions.copy()
                    break
                else:
                    print("There are no incorrect questions to review.")
                    continue
            elif choice == '3':
                exit_game = True
                break
            else:
                print("\nInvalid choice. Enter either 1, 2 or 3.")
                continue

    print("\nGreat study session!\nSee you next time.")

if __name__ == "__main__":
    main()