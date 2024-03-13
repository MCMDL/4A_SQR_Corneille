![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)  

# Frontend

L'intégralité du frontend a été réalisé à l'aide de `HTML`, `CSS` et `JS`

## Aperçu du code

Le code permet de mettre en place certaines des exigences demandées même si le principal fonctionne via des commandes `curl` dans le backend

### Le `HTML`

Le code `HTML` va nous servir à avoir une page internet sur lequel nous baser et voir les modifications appliquées par le `JS`
Le plus important dans le `HTML` est de placer des balises ou ID pour pouvoir les appeler dans le `JS`  
>[!NOTE]
>PS : On a voulu apporter une petite touche d'humour sur notre page web, parce que vous devez en avoir marre de corriger des Twitter bleus classiques. On espère que vous apprécierez !  

### Le `CSS`

Le code `CSS` va nous servir à rendre jolie la page `HTML` et rien de plus 

### Le `JavaScript`

Le `JS` lui va nous servir à faire le lien entre le front et le back mais aussi à modifier le code `HTML` pour afficher les Tweets.
Il y a 3 fonctions principales dans le `JS` :
- `messageAlert`
- `displayTweet`
- `addTweet`

#### Fonction `messageAlert`

Cette fonction permet d'afficher un message d'alerte pour informer l'utilisateur que,
- Le tweet est posté en `vert`
- Le tweet est posté mais il y a eu un problème quelque part en `jaune`
- Le tweet n'est pas posté parce qu'il y a un problème en `rouge`*

#### Fonction `displayTweet`

Cette fonction permet d'afficher le tweet que l'on vient d'écrire sur la page `HTML`, pour cela il va modifier le code `HTML` en ajoutant une balise `<li>` qui contiendra une balise `<div>`.  
Il ne suffit pas seulement de modifier le `HTML` mais il faut aussi récupérer les données du tweet qui sont dans la base de donnée `redis` 

#### Fonction `addTweet`

Cette fonction va récuperer les données mises dans les `textearea` sur la page `HTML` et va ensuite envoyer ces données au backend, dans la base de donnée `redis`
