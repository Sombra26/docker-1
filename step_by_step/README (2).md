
# Tutoriel Git étape par étape

## Créer un repository distant (remote) sur GitHub

- Après s'être inscrit sur Github ([Lien](https://github.com/join?source=login)), se connecter et se rendre sur [la page pour créer un nouveau repository](https://github.com/new). Vous pouvez l'appeler `git_step_by_step`

![Screenshot](images/create_repo_github.png)

- On arrive sur cette page :

![Screenshot](images/repo_created.png)


## Créer un repository en local

- Aller dans le dossier choisi avec le terminal (sur Linux / Mac OS) ou avec Git Bash (Windows) :

	```bash
	cd git_step_by_step/ 
	```

- Initialiser le repository local : 

	```bash
	git init
	```


## Faire un premier commit en local

- Créer un fichier texte `file_1.txt`, par exemple en tapant :

	```bash
	touch file_1.txt
	open file_1.txt # le fichier va s'ouvrir, écrire quelque chose et enregistrer
	```


- Vérifier ce qu'on a modifié :

	```bash
	git status # vérifier ce qu'on a modifié
	```

- Ajouter les modifications faites (c'est dire à Git ce qu'on va sauvegarder dans l'étape d'après). Il faut avoir enregistré à l'étape d'avant ! 

	```bash
	git status # vérifier ce qu'on a modifié
	git add file_1.txt 
	```

- Commit (c'est faire une photo de notre dossier en ne photographiant que ce qu'on a ajouté dans l'étape d'avant)

	```bash
	git commit -m "file_1.txt créé, on a écrit dedans"
	```


## Pousser sur le repository remote pour la première fois

- Ajouter l'URL de la branche en remote (`origin`)

	```bash
	git remote add origin https://github.com/Selimmmm/git_step_by_step.git
	# https://github.com/username/name_of_repository.git dans votre cas
	```


- "Brancher" notre branche `master` (en local) sur la branche `origin` (en remote) et pousser


	```bash
	git push --set-upstream origin master
	```


- Aller sur la page de repository pour voir les modifications en ligne : [https://github.com/Selimmmm/git_step_by_step](https://github.com/Selimmmm/git_step_by_step) (ou https://github.com/username/name_of_repository)



## Routine status / add / commit / push

- Ajouter une ligne dans `file_1.txt` et y écrire quelque chose, et créer et écrire dans `file_2.txt`

	```bash
	open file_1.txt # le fichier va s'ouvrir, écrire quelque chose et enregistrer
	touch file_2.txt
	open file_2.txt # le fichier va s'ouvrir, écrire quelque chose et enregistrer
	```

- Status / Add / Commit / Push

	```bash
	git status # on vérifier les modifications
	git add file_1.txt file_2.txt # on peut utiliser "git add . " pour ajouter toutes les modifications
	git commit -m "Second commit - we modified file_1.txt et created file_2.txt"
	git push
	```


## Créer une nouvelle branche

- Créer une nouvelle branche / changer de branche
	```bash
	git checkout -b new_branch
	git branch # affiche toutes les branches en local
	git checkout master # retourner sur master
	git checkout new_branch # retourner sur new_branch
	```


- En étant dans la branche new_branch, créer un nouveau fichier `file_new_branch.txt`, écrire dedans et enregistrer :

	```bash
	touch file_new_branch.txt
	touch file_new_branch.txt
	git checkout master # retourner sur master
	git checkout new_branch # retourner sur new_branch
	```


- Vérifier les modifications, ajouter et "commit" :

	```bash
	git status # on vérifier les modifications
	git add file_new_branch.txt 
	git commit -m "3rd commit - Commit on new branch - file_new_branch.txt created"
	```



## Merge `new_branch` dans `master`

- On veut fusionner les dernières modifications sur new_branch avec la branche master :

	```bash
	git log # regarder les commits présents sur new_branch
	git checkout master # retourner sur master
	git log # regarder les commits présents sur master (il n'y a pas le dernier qui est sur new_branch)
	git merge new_branch # ajouter les commit fait dans new_branch dans master
	git push # pousser les modifications sur le repository distant
	```


## Pour mieux comprendre

![Screenshot](images/nice_info.png)
