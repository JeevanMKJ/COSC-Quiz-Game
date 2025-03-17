import json
from utils.questions import initial_questions

def convert_questions_to_json():
    # Ensure proper formatting of questions
    formatted_questions = [
        {
            "question": q["question"],
            "options": q["options"],
            "answer": q["answer"],
            "answer_name": q["answer_name"],
            "module": q["module"],
            "explanation": q["explanation"]
        }
        for q in initial_questions
    ]
    
    # Write to JSON file with proper formatting
    with open("questions.json", "w", encoding="utf-8") as f:
        json.dump(formatted_questions, f, indent=4, ensure_ascii=False)
    
    print(f"Successfully converted {len(formatted_questions)} questions to questions.json")

if __name__ == "__main__":
    convert_questions_to_json()
