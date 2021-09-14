import csv
# import os
# from itertools import combinations



class Action:
    """creation action object"""
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit
        self.gain = (price*profit)/100
    
    def __str__(self):
        return f'Nom: {self.name}, Prix:{self.price} €, Profit: {self.profit} %, Gain: {self.gain} €'


def data_set_csv():
    """Open and read the csv file"""
    wallet =[]
    with open('data_set/dataset0.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
	        wallet.append(Action(row[0], int(row[1]), int(row[2])))
    return wallet      

def brute_force(wallet, MAX_INVEST):
    """this function will try to find the best invest """
    # creation de toute les combinaisons d'actions
    
    # choix de la combinaisons <= à 500euro la plus proche (investissement)
    # calcul du gain total de chaques combinaisons
    
    
    pass


def main():
    """"""
    # ouvrir mon fichier dataset.csv
    # lire les datas de mon fichier
    # calculer les gains de chaque actions sur 2 ans ((coût*benef)/100)
    # enregistrer les gains pour chaque actions
    wallet = data_set_csv()
    for wal in wallet:
        print(wal.gain)
    # tester chaques combinaisons possible d'action pour un investisement max de 500€ et une rentabilité maximale
    MAX_INVEST = 500
    soluc_choice = brute_force(wallet, MAX_INVEST)
    # afficher la reponse
    

if __name__ == "__main__":
    main()
    