# OC-QL-P07


***

## 1.Presentation
***
Le but de ce projet est de créer un algorithme rapide en python pour trouver la meilleure combinaison d'actions sur lesquelles investir pour avoir le meilleur bénéfice au bout de 2 ans en prenant en compte les contraintes telles que le montant maximum d'investissement et le prix des actions 


## 2-Installation  :
***
Se diriger sur le repertoire où l'on souhaite installer l'application.

Pour installer le programme via un terminal :  

Sous Windows :  
```sh
$ git clone https://github.com/quentin8469/OC-QL-P07.git  
$ python3 -m venv env  
$ env/scripts/activate  
$ pip3 install -r requirements.txt   
```
Sous linux/Mac :      
```sh
$ git clone https://github.com/quentin8469/OC-QL-P07.git
$ python3 -m venv env    
$ source env/bin/activate    
$ pip3 install -r requirements.txt    
```


## 3-Fonctionnement:
* Fichier brute force:
execution du programme : $ python "???".py /br
Cet algorithme va tester toutes les combinaisons possibles une à une et garder la meilleur (ce qui rend l'exécution très longue).

* Fichier optimisé:
execution du programme : $ python "???".py



***
Créer un rapport flake8 :  

`flake8 --exclude=env,venv --format=html --htmldir=flake8_report --max-line-lengt=119`

