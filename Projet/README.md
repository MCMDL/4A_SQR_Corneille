# Rapport du Projet Cloud
Ce projet a été réalisé par Arnaud Binet et Martin Corneille.  

## Objectifs
Le but de ce projet est de mettre en place un site Tweeter like. Pour cela on utilsera les langages HTML/CSS/JS pour la partie frontend et Python pour la backend. 
L'objectif est de créer des API pour pouvoir réaliser les action suivantes :
- [X] Tweeter
- [ ] Afficher les Tweets
- [ ] Afficher les topics (hashtags)
- [ ] Retweeter
- [ ] Afficher les Tweets liés à un topic
- [ ] Afficher les Tweets d'un utilisateur

## Frontend
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
Informations techniques disponible [ici](/Projet/frontend/README.md).  
Le rôle du frontend est de communiquer avec l'API, on peut donc envoyer des tweets, les afficher ou encore réaliser les actions cités dans la partie Objectifs.

## Backend
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
Informations techniques disponible [ici](/Projet/backend/README.md).  
Le but du backend est de mettre en place les API citées dans la partie Objectifs. Pour cela on utilse la librairie `Flask` et les données sont gérées à l'aide la base de données NoSQL `Redis`.

## Exécuter le projet
Pour lancer le projet il faut réaliser les étapes suivantes : 
- Exécuter le code Python présent dans le backend. ([Le voilà](/Projet/backend/app.py) :upside_down_face:)  
- Exécuter dans le terminal la commande suivante : docker run -p 6379:6379 --name myredis redis
>[!IMPORTANT]
>Erreur possible du au nom du container ne pas hésiter à changer *myredis* par un autre nom.

