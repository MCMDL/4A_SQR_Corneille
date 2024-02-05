from flask import Flask, request, jsonify
import redis

app = Flask(__name__)


r = redis.Redis(host='localhost', port=6379, db=0)


resultats = {}

@app.route("/api/calcul", methods=["POST"])
def calcul():

    data = request.get_json()
    operation = data["operation"]
    operandes = data["operandes"]

    if operation == "+":
        resultat = sum(operandes)
    elif operation == "-":
        resultat = operandes[0] - operandes[1]
    elif operation == "*":
        resultat = 1
        for op in operandes:
            resultat *= op
    elif operation == "/":
        resultat = operandes[0] / operandes[1]

    id = len(r.keys()) + 1
    #resultats[id] = resultat
    r.set(id,resultat)

    return jsonify({"id": id})

@app.route("/api/resultat/<int:id>", methods=["GET"])
def resultat(id):

    #if id not in resultats:
    #    return jsonify({"erreur": "ID inexistant"})

    resultat = r.get(id)
    return jsonify({"resultat": resultat}) #resultats[id]

if __name__ == "__main__":
    app.run(debug=True)
