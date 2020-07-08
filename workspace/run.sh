sudo iptables -t filter -F && sudo iptables -t filter -X && sudo systemctl restart docker
docker-compose up
