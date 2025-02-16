from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Сервер жұмыс істеп тұр!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # Render автоматты түрде порт береді
    app.run(host="0.0.0.0", port=port)
