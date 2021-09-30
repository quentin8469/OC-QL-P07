import csv
import time



class Action:
    """ Create the Action object"""
    
    def __init__(self, name, price, profit):
        self.name = name
        self.price = int(round(float(price)*100))
        self.profit = int(round(float(profit)*100))
        self.gain = int(((self.price*self.profit)/100)*100)

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Profit: {self.profit}'\
               f', Gain: {self.gain}'


def data_set_csv(datafile):
    """Open and read the csv file for create a list of action object"""
    
    wallet =[]
    with open(f'data_set/{datafile}.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if float(row[1]) <= 0.0 or float(row[2]) <= 0.0:
	            del(row)
            else:
                wallet.append(Action(row[0], row[1], row[2]))

    return wallet


def get_matrix(wallet, max_invest):
    """ Generate a empty matrix"""
    
    matrix = []
    for line in range(0, len(wallet)+1):
        tableau_largeur = []
        for column in range(0, max_invest +1):
            tableau_largeur.append(0)
        matrix.append(tableau_largeur)

    return matrix


def algo_opti(wallet, max_invest):
    """ filling the empty matrix with the best gain possible"""
    
    matrice = get_matrix(wallet, max_invest)
    
    for action in range(1, len(wallet)+1):
        for invest in range(1, max_invest+1):
            if wallet[action-1].price <= invest:
                best_pos = wallet[action-1].gain + matrice[action-1][invest-wallet[action-1].price]
                matrice[action][invest] = max(best_pos, matrice[action-1][invest])
            else:
                matrice[action][invest] = matrice[action-1][invest]
    return matrice


def best_option(wallet, max_invest, matrice):
    """ Search the best optimized action solution in the matrix"""
    
    invest = max_invest
    len_wallet = len(wallet)
    optimized_portfolio = []

    while invest >= 0 and len_wallet >= 0:
        action = wallet[len_wallet-1]
        if matrice[len_wallet][invest] == matrice[len_wallet-1][invest- action.price] + action.gain:
            optimized_portfolio.append(action)
            invest -= action.price
            
        len_wallet -=1
    
    return optimized_portfolio


def display_solution(best_portfolio):
    """ view to display the optimized result"""
    
    combi = []
    combi_gain =[]
    total_gain = 0
    total_invest = 0
    
    for action in best_portfolio:
        total_gain += action.gain
        total_invest += action.price
        combi.append(action.name)
        combi_gain.append(action.gain)
    
    return f'La meilleure combinaison d\'action est: {combi}\n'\
           f'Pour un gain estimé de: {total_gain/1000000} €\n'\
           f'Pour un investissement de:{total_invest/100} €\n'\


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

    max_invest = 50000 #conversion euros en centimes *100
    wallet = data_set_csv(csv_file)
    print("------------sac à dos-------------------")
    start_time = time.time()
    sac_a_dos = algo_opti(wallet, max_invest)
    best_portfolio = best_option(wallet, max_invest, sac_a_dos)
    solution = display_solution(best_portfolio)
    print(solution)
    end_time = time.time()
    print('Temps d\'execution:' , (end_time - start_time), 'secondes')
    print("--------------END sac à dos---------------------")



if __name__ == "__main__":
    
    main()