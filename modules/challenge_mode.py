# modules/challenge_mode.py

import openai
import os
import json
from difflib import SequenceMatcher

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_challenge_questions(text):
    prompt = f"""
You are an intelligent assistant. From the following document, generate 3 logic or comprehension-based questions. 
Each question should have:
- question
- correct answer
- justification based on the text

Document:
{text[:3000]}

Respond in this JSON format only:
[
  {{ "question": "...", "answer": "...", "justification": "..." }},
  ...
]
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )

    content = response['choices'][0]['message']['content']

    # Clean and parse JSON safely
    try:
        content = content.strip()
        if content.startswith("```"):
            content = content.strip("`").strip("json").strip()
        questions = json.loads(content)
        return questions
    except Exception as e:
        print(f"[Challenge Mode] JSON Parse Error: {e}")
        return []

def evaluate_user_answer(correct_answer, user_answer):
    """Fuzzy matching to compare similarity"""
    correct = correct_answer.strip().lower()
    user = user_answer.strip().lower()
    score = SequenceMatcher(None, correct, user).ratio()
    return score >= 0.6
