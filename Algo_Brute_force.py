import csv
# import os
# import itertools



class Action:
    """creation action object"""
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit
        self.gain = (price*profit)/100
    
    def __str__(self):
        return f'nom: {self.name}, prix:{self.price} €, profit: {self.profit} %, gain: {self.gain} € '



def data_set_csv():
    """ Open and read the csv file"""
    wallet =[]
    with open('data_set/dataset0.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
	        wallet.append(Action(row[0], int(row[1]), int(row[2])))
    for wal in wallet:
        print(wal)
    return wallet
         


def main():
    """"""
    # ouvrir mon fichier dataset.csv
    wallet = data_set_csv()
    # lire les datas de mon fichier
    # calculer les gains de chaque actions sur 2 ans ((coût*benef)/100)
    # enregistrer les gains pour chaque actions
    # tester chaques combinaisons possible d'action pour un investisement max de 500€ et une rentabilité maximale
    # afficher la reponse
    print(wallet)

if __name__ == "__main__":
    main()
    