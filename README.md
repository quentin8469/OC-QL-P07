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

Pour executer le programme: python main.py <br>
    * Choisisez le script que vous souhaitez lancer.<br>
    1-force brute  2-glouton  3-dynamique
    * Choississez le fichier de données à lire.
    1- dataset0   2-dataset1   3-dataset2

***
Créer un rapport flake8 :  

`flake8 --exclude=env,venv --format=html --htmldir=flake8_report --max-line-lengt=119`

