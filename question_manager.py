import json
import os

class QuestionManager:
    def __init__(self, json_file="questions.json"):
        self.json_file = json_file
        self.questions = self.load_questions()
    
    def load_questions(self):
        """Load questions from JSON file"""
        if not os.path.exists(self.json_file):
            raise FileNotFoundError(f"Questions file {self.json_file} not found")
        
        with open(self.json_file, "r", encoding="utf-8") as f:
            return json.load(f)
    

