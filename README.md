# COSC Chapter Questions Quiz Game

## Description
I am a computer science student at Austin Community College. While preparing for my first exam, I felt there could be a better way to review the multiple-choice questions from the chapters we were tested on. To address this, I developed a Python command-line program containing a list of 70 questions from the textbook.

## Installation
I'm not sure why anyone would want to use this code, as the entire idea is to build one's own projects to learn. However, if you're interested:
- Clone the repository using git clone git@github.com:JeevanMKJ/COSC-Quiz-Game.git
- If desired, you can change the question list. The current questions are from "Tony Gaddis - Starting Out with Python - Pearson".

## Usage
To run the program, execute "python3 cosc_quiz_game.py" in the command line. You will be prompted to enter the number of questions you want to answer. Enter a number between 1 and 70.

When answering questions, enter a, b, c, or d. After the specified number of questions has been asked, your score will be displayed. You will then be presented with three options:
1. Play another set of questions.
2. Review all questions answered incorrectly.
3. Quit the game.

- If you select option 1, the loop starts over.
- If you select option 2, the incorrect questions will be asked again, and you will be presented with the same three options at the end.
- If you select option 3, the game will quit.

## Future
I will likely build more features as I progress in my studies. Some potential enhancements include:
- A user interface (UI).
- Deployment on the web.
- User accounts, login functionality, and the ability to track scores and questions.
- Using MongoDB as a database.
- Integrating Hugging Face to provide short, descriptive answers for all questions answered incorrectly.
