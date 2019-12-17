docker-compose up -d --build
docker exec python_app python qtroid.py
docker exec java_app gradle war
docker exec java_app gradle run
