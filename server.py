from flask import Flask, request, jsonify

app = Flask(__name__)

# Кеңестер базасы
TIPS = {
    "1": "if шартында False болса, else бөлігіндегі код орындалады.",
    "2": "Шартты тексеру үшін if операторы қолданылады.",
    "3": "'==' – теңдік операторы, '=' – меншіктеу операторы.",
    "4": "'age >= 18' дегеніміз – жас 18 немесе одан үлкен деген сөз.",
    "5": "Дұрыс синтаксис: 'if x == 10:'", 
}

# Мотивациялық суреттер
MOTIVATION_IMAGES = {
    "low": "https://example.com/try_again.jpg",
    "medium": "https://example.com/good_job.jpg",
    "high": "https://example.com/excellent.jpg"
}

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    user_answers = data.get("answers", {})
    correct_answers = {
        "1": "b", "2": "b", "3": "b", "4": "b", "5": "c"
    }
    
    correct_count = 0
    feedback = {}
    
    for q_id, user_answer in user_answers.items():
        if user_answer == correct_answers.get(q_id, ""):
            correct_count += 1
        else:
            feedback[q_id] = TIPS.get(q_id, "Кеңес жоқ")
    
    # Мотивациялық суретті таңдау
    if correct_count <= 2:
        image_url = MOTIVATION_IMAGES["low"]
    elif correct_count <= 4:
        image_url = MOTIVATION_IMAGES["medium"]
    else:
        image_url = MOTIVATION_IMAGES["high"]
    
    return jsonify({
        "correct_count": correct_count,
        "feedback": feedback,
        "image": image_url
    })

if __name__ == '__main__':
    app.run(debug=True)
