import os
from flask import Flask, jsonify, Response

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "TV KIDS MONDE LIVE")

@app.route("/")
def home():
    return Response("""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TV KIDS MONDE LIVE</title>
<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #e8f7ff;
    color: #12304a;
    text-align: center;
}
header {
    background: #078bd5;
    color: white;
    padding: 25px 10px;
}
main { padding: 20px; }
.card {
    max-width: 600px;
    margin: 20px auto;
    padding: 20px;
    background: white;
    border-radius: 16px;
    box-shadow: 0 4px 14px #0002;
}
.badge {
    display: inline-block;
    background: #d5f8e4;
    color: #08763b;
    padding: 8px 14px;
    border-radius: 20px;
}
footer { padding: 20px; color: #536b7c; }
</style>
</head>
<body>
<header>
<h1>📺 TV KIDS MONDE LIVE</h1>
<p>Le monde des enfants, dans un seul espace !</p>
</header>
<main>
<div class="card">
<h2>Bienvenue !</h2>
<p>Notre plateforme de télévision est en préparation.</p>
<p class="badge">Serveur en ligne</p>
</div>
<div class="card">
<h3>🧒 Kids · 🎵 Musique · 🌍 Découverte</h3>
<p>Les chaînes et vidéos seront ajoutées lorsqu'elles seront disponibles
avec les autorisations de diffusion nécessaires.</p>
</div>
</main>
<footer>TV KIDS MONDE LIVE © 2026</footer>
</body>
</html>
""", mimetype="text/html")

@app.route("/health")
def health():
    return jsonify(status="ok", application=APP_NAME)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
