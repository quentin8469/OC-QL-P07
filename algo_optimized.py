import csv
from itertools import combinations
from os import name



class Action:
    """ Creation de l'objet action"""
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit
        self.gain = price*profit/100
        
    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Profit: {self.profit}, Gain: {self.gain}'


def data_set_csv(datafile):
    """Open and read the csv file"""
    wallet =[]
    with open(f'data_set/{datafile}.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if float(row[1]) <= 0.0 or float(row[2]) <= 0.0:
	            pass
            else:
                wallet.append(Action(row[0], float(row[1]), float(row[2])))
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
           f'Pour un investissement de:{total_invest} €'


# def glouton_two(wallet, max_invest):
#     """try to find a good invest"""
#     #trier les objets action par gain possible
#     best_combination = []
#     total_gain = 0
#     total_invest = 0
#     i = 0
#     wallet_tri = sorted(wallet, key=lambda x:x.profit, reverse=True)
#     while i < len(wallet):
#         invest = total_invest + wallet_tri[i].price
#         if invest <= max_invest:
#             total_invest = invest
#             total_gain += wallet_tri[i].gain
#             best_combination.append(str(wallet_tri[i]))
#         i +=1     

#     return f'La meilleure combinaison d\'action est: {best_combination}\n'\
#            f'Pour un gain estimé de: {total_gain} €\n'\
#            f'Pour un investissement de:{total_invest} €'



# def opti_dynamique(wallet, max_invest):
#     """ Algo optimized"""
#     matrice = [[0 for x in range(max_invest + 1)] for x in range(len(wallet) + 1)]
#     print('bob')
#     for i in range(1, len(wallet) + 1):
#         print('bob1')
#         for w in range(1, max_invest + 1):
#             print('bob2')
#             if wallet[i-1].price <= w:
#                 print('bob3')
#                 matrice[i][float(w)] = max(wallet[i-1].profit + matrice[i-1][w-wallet[i-1].price], matrice[i-1][float(w)])
#                 print('bob4')
#             else:
#                 matrice[i][w] = matrice[i-1][w]

#     # Retrouver les éléments en fonction de la somme
#     w = max_invest
#     n = len(wallet)
#     elements_selection = []

#     while w >= 0 and n >= 0:
#         e = wallet[n-1]
#         if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
#             elements_selection.append(e)
#             w -= e[1]

#         n -= 1
#     return matrice[-1][-1], elements_selection

def optimized_algo(wallet, max_invest):
    """ optmized algo"""
    matrice = [[0 for x in range(max_invest + 1)] for x in range(len(wallet) + 1)]
    print(matrice)
    


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
    
    max_invest = 500        
    wallet = data_set_csv(csv_file)
    opti_invest = glouton(wallet, max_invest)
    print(opti_invest)
    #opti_invest_two = glouton_two(wallet, max_invest)
    print("----------------------------------------------")
    #print(opti_invest_two)
    opti_dyna = optimized_algo(wallet, max_invest)
    print("----------------------------------------------")
    print(opti_dyna)
    

if __name__ == "__main__":
    """"""
    main()