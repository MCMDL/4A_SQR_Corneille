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

#API pour recupérer toutes les données liées à un tweet
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
    #Ajout du Tweet à l'utilisateur
    userKey = "u-"+username
    r.rpush(userKey,idTweet)


    #Récupération des Hashtag dans le tweet
    idHash = r.get("idHash")
    if idHash==None:
        r.set("idHash",0)
    idHash = int(r.get("idHash"))
    idHash = idHash +1
    hashtags = foundHashtag(tweet)
    #Verification de la présence de hashtags
    if len(hashtags)!=0:
        for hashtag in hashtags:
            #Création de la clef pour stocker les hastags
            hashKey = "h-" + hashtag
            #Stockage du nom du topic s'il n'existe pas
            if r.lindex(hashKey,0)==None:
                r.rpush("hashList", hashtag)
                idHash = idHash + 1
            #Ajout du tweet
            r.rpush(hashKey,idTweet)
            print("Sujet : " + hashtag + "\n")
    r.set("idHash",idHash)
    #Affichage des infos récupérées + return
    print(username+"\n")
    print(tweet)
    temp = "Tweet ajouté : " + tweet +" By :" + username +" Id is : " + str(idTweet)

    return temp

#API pour retourner tous les tweets connus
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


#API pour retourner tous les tweets d'un utlisateur
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

#API pour retweeter
@app.route("/api/retweet", methods=["POST"])
def retweet(idTweet,username):
    userKey = "u-"+username
    #Ajout du tweet à l'utilisateur qui retweet
    for i in range(r.llen(userKey)):
        if r.lindex(userKey,i) == idTweet:
            return "ERROR : Tweet already retweeted"
    r.rpush(userKey, idTweet)
    return "Tweet retweeted"
    


#API pour retourner un tweet particulier
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


#API pour afficher tous les  hashtags connus
@app.route("/api/printTopic", methods=["GET"])
def printTopic():
    #Recuperation du dernier idHash
    numberOfHashtags = int(r.get("idHash"))
    hashtags = []
    #Récupération de tous les hashtags dans une liste
    for i in range(numberOfHashtags):
        hashtags.append(r.lindex("hashList",i))
    #Renvoie des hashtags au format JSON
    return json.loads(str(hashtags))

#Récupération de tous les tweets liés à un hashtag
@app.route("/api/printTweetsTopic", methods=["GET"])
def printTweetsTopic(hashtag):
    #Recuperation de la hashKey
    hashkey = "h-" + hashtag
    tweets = []
    index = 0
    #Recuperation de tous les tweets liés à un tag
    while r.lindex(hashkey, index) != None:
        tweets.append(r.lindex(hashkey, index))
        index = index +1
    return json.loads(str(tweets))

if __name__ == "__main__":
    app.run(debug=True)
