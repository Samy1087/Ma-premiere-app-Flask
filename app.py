from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/prenom")
def bonjour():
    """Cette route accueille l'utilisateur"""
    prenom = "Ndeye"
    return render_template("menu.html", prenom=prenom)

@app.route("/<int:a>/<int:b>")
def calcul(a, b):
    """Cette route fais les calculs."""
    return f"{a} + {b} = {a+b}"

@app.route("/date_heure")
def heure():
    """Cette route affiche l'heure actuelle"""
    date = datetime.datetime.now()
    heure = date.hour
    minute = date.minute
    seconde = date.second
    return render_template("date_heure.html", heure=heure, minute=minute, seconde=seconde)

@app.route("/")
def menu():
    """Menu principal"""
    return render_template("index.html")

# Point d'entrée du programme.

if __name__ == "__main__":
    app.run(debug=True)