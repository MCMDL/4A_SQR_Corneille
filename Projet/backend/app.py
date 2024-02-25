from flask import Flask, request, jsonify
import redis
import json
app = Flask(__name__)



r = redis.Redis(host='localhost', port=6379, db=0,decode_responses=True)

def foundHashtag(str1):
    list1 = str1.split(" ")
    topic = []
    for value in list1:
        temp = value.find("#")
        if temp != -1:
            temp = value.split("#")
            topic.append(temp[1])
    return topic

resultats = {}

@app.route("/api/tweeter", methods=["POST"])
def tweeter():
    #Creation de l'ID du tweet
    idTweet = r.get("idTweet")
    if idTweet==None:
        r.set("idTweet",0)
    idTweet = int(r.get("idTweet"))
    idTweet = idTweet +1
    r.set("idTweet",idTweet)
    #Recuperation des données puis création du stockage des tweets
    data = request.get_json()
    tweet = data["tweet"]
    username = data["username"]
    # Dictionnaire JSON pour stocker username et tweet
    dico = json.dumps({"utilisateur": username, "message": tweet})
    # Stockage dans Redis
    r.set(idTweet, dico)
    #value={"author": username, "tweet": tweet }
    #Ajout du Tweet à l'utilisateur
    userKey = "u-"+username
    r.rpush(userKey,idTweet)
    #Ajouter de quoi extraire les "#" fonction findall(r"#\w+", tweet)
    print(username+"\n")
    print(tweet)
    temp = "Tweet ajouté : " + tweet +" By :" + username +" Id is : " + str(idTweet)
    return temp


@app.route("/api/printTweet", methods=["GET"])
def printTweet():
    idTweet = int(r.get("idTweet"))
    print(idTweet)
    if idTweet == None:
        return "ERROR: Tweet doesn't exist"
    temp = ""
    for i in range (1,idTweet): 
        tweet = str(r.get(i))
        temp = temp + tweet +"\n"
    return temp
        # if tweet != None:
        #     print(tweet)
        #     # Désérialisation de la valeur JSON
        #     dataFinale = json.loads(tweet)
        #     temp = temp + dataFinale + "\n"
        #     return temp
        # else: 
        #     print("ERROR: JSON value is empty")
        #     return "ERROR: JSON value is empty"

    

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
