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
            if row[1] > '0' and row[2] > '0':
	            wallet.append(Action(row[0], float(row[1]), float(row[2])))
            # else:
            #     wallet.append(Action(row[0], float(row[1]), float(row[2])))
                
    return wallet


def glouton(wallet, max_invest):
    """try to find a good invest"""
    #trier les objets action par gain possible
    best_combination = []
    total_gain = 0
    total_invest = 0
    wallet_tri = sorted(wallet, key=lambda x:x.profit, reverse=True)
    for wallet in wallet_tri:
        invest = total_invest + wallet.price
        if invest <= max_invest and wallet.gain >0:
            total_invest = invest
            total_gain += wallet.gain
            best_combination.append(str(wallet))     

    return f'La meilleure combinaison d\'action est: {best_combination}\n'\
           f'Pour un gain estimé de: {total_gain} €\n'\
           f'Pour un investissement de:{total_invest/100} €'


def glouton_two(wallet, max_invest):
    """try to find a good invest"""
    #trier les objets action par gain possible
    best_combination = []
    total_gain = 0
    total_invest = 0
    i = 0
    wallet_tri = sorted(wallet, key=lambda x:x.profit, reverse=True)
    while i < len(wallet):
        invest = total_invest + wallet_tri[i].price
        if invest <= max_invest:
            total_invest = invest
            total_gain += wallet_tri[i].gain
            best_combination.append(str(wallet_tri[i]))
        i +=1     

    return f'La meilleure combinaison d\'action est: {best_combination}\n'\
           f'Pour un gain estimé de: {total_gain} €\n'\
           f'Pour un investissement de:{total_invest/100} €'

def optimized_algo(wallet, max_invest):
    """"""
    
    #nb_action = len(wallet)
    # creation de la matrice,initialisation à 0,les +1 ajoute ligne et colonne à 0
    mat = [[0 for x in range(max_invest + 1)] for x in range(len(wallet) )]
    print(len(mat))
    #je parcours les actions(lignes)
    for item in range(1, len(wallet) + 1):
        #print(item)
        #print(mat[-10][-10])
        # pour chaque item je parcours leurs prix (colonnes)
        for euro in range(1, max_invest + 1):
            #print(mat)
            #print(euro)
            # si mon prix est inferieur a max_invest 
            if wallet[item - 1].price <= euro:
                #alors je compars le resultat optimisé de la ligne d'avant avec le resultat courant
                mat[item][euro] = max(wallet[item - 1].profit + mat[item - 1][euro - wallet[item - 1].price], mat[item - 1][euro])
                #print(mat[item][euro])
            else:
                # si la nouvelle action depasse le max invest, alors je garde la ligne d'avant
                mat[item][euro] = mat[item - 1][euro]
                
    
    # Retrouver les éléments en fonction de la somme
    # on pars de invest et n qui correspond a la derniere case de la matrice
    invest = max_invest
    n = len(wallet)
    combinaison = []
    
    # combi = []
    # total_gain = 0
    # total_invest = 0
    # tant que invest est sup à 0 et que la liste est sup len(wallet)
    while invest >= 0 and n >= 0:
        #on prend le dernier element de la matrice
        action_list = wallet[n-1]
        #print(wallet[n-1])
        if mat[n][invest] == mat[n-1][invest- action_list.price + action_list.profit]:
            print('bob')
            # on ajoute l'action choisie
            combinaison.append(action_list.name)
            #print(combi)
            invest -= action_list.price
            
        n -= 1
    
    # for action in combinaison:
    #     total_gain += action.gain
    #     total_invest += action.price
    #     combi.append(action.name)
    
    return f'La meilleure combinaison d\'action est: {combi}\n'\
           f'Pour un gain estimé de: {total_gain} €\n'\
           f'Pour un investissement de:{total_invest} €'

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
    # print("------------glouton_one-------------------")
    # algo_optimized_one = glouton(wallet, max_invest)
    # print(algo_optimized_one)
    # print("----------------------------------------------")
    # print("--------------END glouton_one---------------------")
    # print("----------------------------------------------")
    # print("------------glouton_two-------------------")
    # opti_invest_two = glouton_two(wallet, max_invest)
    # print(opti_invest_two)
    # print("----------------------------------------------")
    # print("--------------END glouton_two---------------------")
    # print("----------------------------------------------")
    # print("------------sac à dos-------------------")
    # print("----------------------------------------------")
    sac_a_dos = optimized_algo(wallet, max_invest)
    # print(sac_a_dos)
    # print("--------------END sac à dos---------------------")
    # print("----------------------------------------------")


if __name__ == "__main__":
    """"""
    main()