#Commandes à éxécuter : 

1- docker run -p 6379:6379 --name myredis redis
2- docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management
3- curl -X POST -H "Content-Type: application/json" \-d '{"tweet": "salut ceci est un tweet", "username": "Michel"}' \https://jubilant-space-orbit-wqq47rrjpvr29gx5-5000.app.github.dev:5000/api/tweeter