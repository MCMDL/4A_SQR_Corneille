![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)  

# API Python 
Toutes les API ont été créées avec `Flask` et utilisent `Reddis` pour stocker les données

## Aperçu du code
Le code met en place les fonctions nécessaires pour répondre aux exigeances définies pour le projet.  
Nous avons donc définis les fonctions suivantes : 
- `tweeter`
- `printTweet`
- `printPersonnalTweet`
- `retweet`
- `printSpecificTweet`
- `printTopic`
- `printTweetsTopic`  

Toutes les fonctions se trouvent après le chemin `api/`.

### Fonction `tweeter`
Cette fonction sert à récupérer les informations présentes dans un Tweet i.e, le Tweet, l'utilisateur, et les hashtags présents dans le Tweet. Elle est basée sur un `POST`
- Un Tweet est stocké à l'aide d'une clef qui est un entier. Le dernier ID utilisé est stocké à l'aide de la clef `"idTweet"`.
- L'utilisateur et ses tweets sont sauvegardés sous une clef de la forme `u-username` à laquelle on y ajoute la liste des IDs de ses Tweets.
- Les hashtags sont enregitrés avec une clef de la forme `h-hashtag` auquel on ajoute la liste des Tweets avec ce hashtag. La liste de tous les hashtags est stockés avec la clef `"hashList"`

### Fonction `printTweet` 
Cette fonction utilisant un `GET` ressort tous les tweets déja stockés. Elle est utile pour récupérer les Tweets pour les afficher sur la page d'accueil.

### Fonction `printPersonnalTweet`
Cette fonction utilise un `GET` et  nécessite en entrée un username. A l'aide de cet input on recrée la clef `u-username` et on ressort tous les tweets associés à l'utilisateur.

### Fonction `retweet`
Cette méthode basée sur `POST` sert à retweeter un Tweet. Elle ajoute à l'utilisateur un tweet qui n'est originellement pas le sien à sa liste de Tweets.

### Fonction `printSpecificTweet`
Cette méthode utilise un `GET` et à partir d'un ID donné en entrée elle ressort le Tweet associé à cet ID.

### Fonction `printTopic`
Cette méthode basée sur un `GET` retourne tous les hashtags enregistrés i.e toutes les valeurs stockées avec la clef `hashList`.

### Fonction `printTweetTopic`
Cette méthode basée sur un `GET` retourne tous les Tweets liées à un sujet en particulier. Elle nécessite un sujet en input.
