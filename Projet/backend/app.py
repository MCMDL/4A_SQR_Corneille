from flask import Flask, request, jsonify
import redis

app = Flask(__name__)


r = redis.Redis(host='localhost', port=6379, db=0)


resultats = {}

@app.route("/api/tweeter", methods=["POST"])
def tweeter():

@app.route("/api/printTweet", methods=["GET"])
def resultat(id):

@app.route("/api/saveTweet", methods=["POST"])
def resultat(id):

@app.route("/api/printPersonnalTweet", methods=["GET"])
def resultat(id):

@app.route("/api/Retweet", methods=["POST"])
def resultat(id):

@app.route("/api/printTopic", methods=["GET"])
def resultat(id):

@app.route("/api/printSpecificTweet", methods=["GET"])
def resultat(id):

if __name__ == "__main__":
    app.run(debug=True)
