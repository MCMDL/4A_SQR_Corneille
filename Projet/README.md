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
Informations techniques disponible [ici](\frontend\README.md).  
Le rôle du frontend est de communiquer avec l'API, on peut donc envoyer des tweets, les afficher ou encore réaliser les actions cités dans la partie Objectifs.

## Backend
Informations techniques disponible [ici](\backend\README.md).  
Le but du backend est de mettre en place les API citées dans la partie Objectifs. Pour cela on utilse la librairie `Flask` et les données sont gérées à l'aide la base de données NoSQL `Reddis`. 
