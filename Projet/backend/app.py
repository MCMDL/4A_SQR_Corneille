from flask import Flask, request
from flask_cors import CORS
import redis
import re
import json

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
CORS(app)

@app.route("/api/tweeter", methods=["POST"])
def tweeter():
    # Récupération des données JSON envoyées
    data = request.get_json()
    username = data["username"]
    tweet = data["message"]
    
    # Incrémentation de l'ID du tweet
    tweet_id = r.incr("idTweet")

    # Création du dictionnaire tweet_data
    tweet_data = {
        "id": tweet_id,
        "author": username,
        "hashtags": re.findall(r'#\w+', tweet),
        "message": tweet,
        "retweets": []
    }

    # Stockage du tweet dans Redis
    r.set(f'tweet:{tweet_id}', json.dumps(tweet_data))
    r.lpush('tweets', tweet_id)

    # Ajout du tweet à l'utilisateur
    userKey = "u-" + username
    r.rpush(userKey, tweet_id)

    # Ajout des hashtags à Redis
    for hashtag in tweet_data["hashtags"]:
        r.lpush(f'hashtag:{hashtag}', tweet_id)
        if r.lpos('hashtags', hashtag) is None:
            r.lpush('hashtags', hashtag)

    return { "success": True }

@app.route("/api/printTweet", methods=["GET"])
def printTweet():
    #Recuperation du dernier id de tweet
    numberOfTweet = int(r.get("idTweet"))
    tweets = []
    #Récupération de tous les tweets dans une liste
    for i in range(numberOfTweet):
        tweets.append(r.get(i))
    #Renvoie des tweets au format JSON
    return json.loads(str(tweets))



@app.route("/api/printPersonnalTweet", methods=["GET"])
def printPersonnalTweet(username):
    tweets = []
    userKey = "u-"+username
    #Ajout de tous les tweets à une liste 
    for i in range(r.llen(userKey)):
        index = r.lindex(userKey,i)
        tweets.append(r.get(index))
        print(r.get(index))
    #Passage de la liste en Json pour la retourner
    jsonList= json.loads(str(tweets))
    return jsonList

@app.route("/api/retweet", methods=["POST"])
def retweet(idTweet,username):
    userKey = "u-"+username
    #Ajout du tweet à l'utilisateur qui retweet
    for i in range(r.llen(userKey)):
        if r.lindex(userKey,i) == idTweet:
            return "ERROR : Tweet already retweeted"
    r.rpush(userKey, idTweet)
    return "Tweet retweeted"
    

# @app.route("/api/printTopic", methods=["GET"])
# def printTopic(id):

@app.route("/api/printSpecificTweet", methods=["GET"])
def printSpecificTweet(idTweet):
    #Recuperation du dernier id de tweet
    numberOfTweet = int(r.get("idTweet"))
    print(idTweet)
    #Verification de l'existence du tweet
    if idTweet == None or idTweet <0 or idTweet>=numberOfTweet:
        return "ERROR: Tweet doesn't exist"
    temp = r.get(idTweet)
    return temp

if __name__ == "__main__":
    app.run(debug=True)
