- Bâtir l'image simple-webserver sur la base
de tout le contenu du dossier simple-webserver (d'où le ./)
```
docker build -t simple-webserver .
```

- Lancer un conteneur en connectant le port 8000 du conteneur au port 8000 de l'hôte
```
docker run -p 8000:8000 simple-webserver
```

- Se rendre sur localhost:8000