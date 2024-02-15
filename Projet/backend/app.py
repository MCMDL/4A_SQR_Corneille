from flask import Flask, request, jsonify
import redis
import time 

app = Flask(__name__)


r = redis.Redis(host='localhost', port=6379, db=0)


resultats = {}

@app.route("/api/tweeter", methods=["POST"])
def tweeter():
    #Ajout d'un tweet a Redis
    ts = time.time()
    data = request.get_json()
    tweet = data["tweet"]
    username = data["username"]
    value='{"author": username, "tweet": tweet }'
    r.set(ts, value)
    #Ajout du Tweet à l'utilisateur
    userKey = "u-"+username
    #CHANGER POUR METTRE JSON A LA PLACE DE LA LISTE
    r.rpush(userKey,ts)
    #Ajouter de quoi extraire les "#"
    print(username+"\n")
    print(tweet)
    return "tweet ajouté"


# @app.route("/api/printTweet", methods=["GET"])
# def printTweet(id):

# @app.route("/api/saveTweet", methods=["POST"])
# def saveTweet(id):

# @app.route("/api/printPersonnalTweet", methods=["GET"])
# def printPersonnalTweet(id):

# @app.route("/api/retweet", methods=["POST"])
# def retweet(id):

# @app.route("/api/printTopic", methods=["GET"])
# def printTopic(id):

# @app.route("/api/printSpecificTweet", methods=["GET"])
# def printSpecificTweet(id):

if __name__ == "__main__":
    app.run(debug=True)
