Repo pour exercices Cours Docker

Test bind-mount
Créer un conteneur en mode interactif
docker run --rm -t -i -v $(pwd)/persistent:/persistent debian
Écrire depuis le conteneur
echo 'lala' > persistent/file.txt
Vérifier (depuis l'hôte):
ls persistent