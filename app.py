
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Shri Krishna | Divine Peace</title>
        <style>
            body {
                margin: 0;
                font-family: Georgia, serif;
                background: linear-gradient(135deg, #071b33, #174b70, #7b4a92);
                color: white;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                padding: 20px;
                box-sizing: border-box;
            }
            .card {
                max-width: 650px;
                padding: 45px 30px;
                border: 1px solid #e5c878;
                border-radius: 22px;
                background: rgba(255, 255, 255, 0.08);
                box-shadow: 0 10px 40px #0005;
            }
            .feather { font-size: 55px; }
            h1 { color: #f6d77a; font-size: 42px; }
            .quote {
                font-size: 22px;
                line-height: 1.7;
                font-style: italic;
            }
            .meaning {
                color: #e8dff5;
                line-height: 1.8;
            }
            .footer {
                margin-top: 28px;
                color: #f6d77a;
                letter-spacing: 2px;
            }
        </style>
    </head>
    <body>
        <main class="card">
            <div class="feather">🦚</div>
            <h1>Shri Krishna</h1>
            <p class="quote">
                "Whenever you feel lost, remember that
                you are never walking alone."
            </p>
            <p class="meaning">
                Let go of your worries. Do your duty with love,
                keep faith in the journey, and trust that every
                difficult moment can teach you something.
            </p>
            <h2>हरे कृष्ण हरे कृष्ण</h2>
            <p class="footer">RADHE RADHE 💙</p>
            <p>Hosted with love on AWS EC2</p>
        </main>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
