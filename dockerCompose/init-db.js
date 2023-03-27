db = db.getSiblingDB("akopytsiadb");
db.andriicollect.drop();

db.andriicollect.insertMany([
    {
        "id": 1,
        "name": "Easy",
        "type": "Docker"
    },
    {
        "id": 2,
        "name": "Medium",
        "type": "DockerCompose"
    },
    {
        "id": 3,
        "name": "Hard",
        "type": "Kubernetes"
    },
]);