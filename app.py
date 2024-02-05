from flask import Flask, request, jsonify

app = Flask(__name__)

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

    id = len(resultats) + 1
    resultats[id] = resultat

    return jsonify({"id": id})

@app.route("/api/resultat/<int:id>", methods=["GET"])
def resultat(id):

    if id not in resultats:
        return jsonify({"erreur": "ID inexistant"})

    return jsonify({"resultat": resultats[id]})

if __name__ == "__main__":
    app.run(debug=True)
