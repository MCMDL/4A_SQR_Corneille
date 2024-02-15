from flask import Flask, request, jsonify
import redis

app = Flask(__name__)


r = redis.Redis(host='localhost', port=6379, db=0)
resultats = {}

@app.route("/api/tweeter", methods=["POST"])
def tweeter():
    return

@app.route("/api/printTweet", methods=["GET"]) #Afficher les tweets
def printTweet(id):
    return 

@app.route("/api/saveTweet", methods=["POST"])
def saveTweet(id):
    return

@app.route("/api/printPersonnalTweet", methods=["GET"])
def printPersonnalTweet(id):
    return

@app.route("/api/retweet", methods=["POST"])
def retweet(id):
    return

@app.route("/api/printTopic", methods=["GET"])
def printTopic(id):
    return

@app.route("/api/printSpecificTweet", methods=["GET"])
def printSpecificTweet(id):
    return

if __name__ == "__main__":
    app.run(debug=True)
