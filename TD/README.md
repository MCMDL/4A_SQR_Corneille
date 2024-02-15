# 4A_SQR_Corneille_Binet


curl -X POST -H "Content-Type: application/json" \-d '{"operation": "+", "operandes": [2, 3]}' \http://localhost:5000/api/calcul

redis-cli KEYS *

redis-cli GET id1

docker run -p 6379:6379 --name myredis redis

curl -X POST -H "Content-Type: application/json" \-d '{"operation": "+", "operandes": [2, 3]}' \https://jubilant-space-orbit-wqq47rrjpvr29gx5-5000.app.github.dev/:5000/api/calcul