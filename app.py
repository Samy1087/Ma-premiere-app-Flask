from flask import Flask

app = Flask(__name__)

@app.route("/<prenom>")
def bonjour(prenom):
    """Cette route acceuille l'utilisateur"""
    return f"<p>Bienvenue {prenom} sur mon site !</p>"

@app.route("/<int:a>/<int:b>")
def calcul(a, b):
    """Cette route fais les calculs."""
    return f"{a} + {b} = {a+b}"

# Point d'entrée du programme.

if __name__ == "__main__":
    app.run(debug=True)