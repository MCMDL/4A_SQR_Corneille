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
    #Ajout d'un tweet a Redis
    idTweet = r.get("idTweet")
    if idTweet==None:
        r.set("idTweet",0)
    idTweet = int(r.get("idTweet"))
    idTweet = idTweet +1
    data = request.get_json()
    tweet = data["tweet"]
    username = data["username"]
    value='{"author": username, "tweet": tweet }'
    r.set(idTweet, value)
    #Ajout du Tweet à l'utilisateur
    userKey = "u-"+username
    r.rpush(userKey,idTweet)

    # listTs = r.get(userKey)
    # if listTs == None:
    #     liste = [id]
    #     listeJson  = json.loads(str(liste))
    #     r.set(userKey, listeJson)
    # else:
    #     liste = json.dumps(listTs)
    #     liste.append(id)
    #     listeJson = json.loads(str(liste))
    #     r.set(userKey, listeJson)



    #Ajouter de quoi extraire les "#" fonction findall(r"#\w+", tweet)
    print(username+"\n")
    print(tweet)
    temp = "Tweet ajouté : " + tweet +" By :" + username
    return temp


@app.route("/api/printTweet", methods=["GET"])
def printTweet(id):
    value = r.get(id)
    if value == None:
        return "ERROR: Tweet doesn't exist"
    tweet = value[tweet]
    return tweet
    

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
