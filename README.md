# COSC Chapter Questions Quiz Game

## Description
A Python command-line quiz application designed for computer science students at Austin Community College. This program allows students to test their knowledge through multiple-choice questions organized by modules from "Tony Gaddis - Starting Out with Python - Pearson".

## Features
- **Module Selection**: Choose specific chapters or test across all modules
- **Customizable Quiz Length**: Select number of questions per session
- **Review System**: Practice previously incorrect questions
- **Random Questions**: Questions are randomly selected each time
- **Progress Tracking**: View scores after each quiz session

## Installation
1. Clone the repository:
```bash
git clone git@github.com:JeevanMKJ/COSC-Quiz-Game.git
```

2. Navigate to project directory:
```bash
cd COSC-Quiz-Game
```

## Usage
1. Start the program:
```bash
python3 index.py
```

2. Quiz Flow:
   - Select a module or choose "All modules" (0)
   - Enter desired number of questions
   - Answer each question with 'a', 'b', 'c', or 'd'
   - View your score
   - Choose to:
     1. Start new quiz
     2. Review incorrect answers
     3. Exit program

## Project Structure
```
COSC-Quiz-Game/
├── index.py         # Main program entry point
├── quiz_actions.py  # Core quiz functionality
└── questions.py     # Question database
```

## Code Organization
- `index.py`: Main program loop and user interaction
- `quiz_actions.py`: Contains core functions:
  - `get_module_selection()`: Module selection interface
  - `get_num_questions()`: Question quantity selection
  - `handle_quiz_session()`: Quiz execution logic
  - `get_next_action()`: Post-quiz options
- `questions.py`: Question database and module organization

## Future Enhancements
- [ ] Graphical user interface (GUI)
- [ ] Update the dataset from a py to JSON or SQL
- [ ] Web deployment
- [ ] User authentication system
- [ ] Score tracking and statistics
- [ ] MongoDB integration
- [ ] AI-powered explanations using Hugging Face

## Contributing
While this project is primarily for personal educational use, suggestions and improvements are welcome through issues or pull requests.

## License
[MIT License](https://opensource.org/licenses/MIT)

## Author
Jeevan Morgan Kress-Jones
- GitHub: [@JeevanMKJ](https://github.com/JeevanMKJ)
