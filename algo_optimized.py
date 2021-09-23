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
           f'Pour un investissement de:{total_invest} €'

# def optimized_algo(wallet, max_invest):
#     """"""
#     invest = int(max_invest)
#     nb_action = len(wallet)
#     mat = [[0 for x in range(invest + 1)] for x in range(nb_action + 1)]
#     for item in range(1, nb_action+1, 1):
#         for euro in range(1, invest + 1):
#             if wallet[item-1].price <= euro:
#                 mat[item][euro] = max(wallet[item-1].profit + mat[item-1][euro-wallet[item-1].price], mat[item-1][euro])
#             else:
#                 mat[item][euro] = mat[item-1][euro]
    
#     p = int(max_invest)
#     n = len(wallet)
#     combinaison = []
#     combi = []
#     total_gain = 0
#     total_invest = 0
    
#     while p >=0 and n>=0:
#         action_list = wallet[n-1]
#         if mat[n][p] == mat[n-1][p-action_list.price] + action_list.profit:
#             combinaison.append(action_list)
#             p -= action_list.price
#         n -= 1
    
#     for action in combinaison:
#         total_gain += action.gain
#         total_invest += action.price
#         combi.append(action.name)
    
#     return f'La meilleure combinaison d\'action est: {combi}\n'\
#            f'Pour un gain estimé de: {total_gain} €\n'\
#            f'Pour un investissement de:{total_invest} €'

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
    print("------------glouton_one-------------------")
    algo_optimized_one = glouton(wallet, max_invest)
    print(algo_optimized_one)
    print("----------------------------------------------")
    print("--------------END glouton_one---------------------")
    print("----------------------------------------------")
    print("------------glouton_two-------------------")
    opti_invest_two = glouton_two(wallet, max_invest)
    print(opti_invest_two)
    print("----------------------------------------------")
    print("--------------END glouton_two---------------------")
    print("----------------------------------------------")
    # print("------------sac à dos-------------------")
    # print("----------------------------------------------")
    # sac_a_dos = optimized_algo(wallet, max_invest)
    # print(sac_a_dos)
    # print("--------------END sac à dos---------------------")
    # print("----------------------------------------------")


if __name__ == "__main__":
    """"""
    main()