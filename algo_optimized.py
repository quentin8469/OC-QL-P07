import csv
from itertools import combinations
from os import name



class Action:
    """ Creation de l'objet action"""
    def __init__(self, name, price, profit):
        self.name = name
        self.price = int(float(price))
        self.profit = int(float(profit))
        self.gain = self.price*self.profit/100
        
    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Profit: {self.profit}, Gain: {self.gain}'


def data_set_csv(datafile):
    """Open and read the csv file"""
    wallet =[]
    with open(f'data_set/{datafile}.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if float(row[1]) <= 1.0 or float(row[2]) <= 1.0:
	            del(row)    
            else:
                wallet.append(Action(row[0], float(row[1]), float(row[2])))
                
    return wallet


def algo_sac_a_dos(wallet, max_invest):
    """"""
    #je veux créer une matrice vide
    #je veux remplir ma matrice( liste de liste)
    #je veux comparer les possibilitées
    #je veus recuperer la meilleures possibilitées
    #je veux renvoyer le resultat
    pass

def main():
    """"""
    
    print("----------------------------------------------")
    print("             Programme Optimized              ")
    print("----------------------------------------------")
    print("1:dataset0   2:dataset1_Python+P7   3:dataset2_Python+P7")
        
    algo = input("Entrez votre choix et appuyez sur entrée: ")
    if algo == '1':
        csv_file = 'dataset0'
    elif algo == '2':
        csv_file = 'dataset1_Python+P7'
    elif algo == '3':
        csv_file = 'dataset2_Python+P7'
    
    max_invest = 500 #conversion euros en centimes *100
    wallet = data_set_csv(csv_file)
    for x in wallet:
        print(x)
    print("------------sac à dos-------------------")
    print("----------------------------------------------")
    sac_a_dos = algo_sac_a_dos(wallet, max_invest)
    print(sac_a_dos)
    print("--------------END sac à dos---------------------")
    print("----------------------------------------------")


if __name__ == "__main__":
    """"""
    main()