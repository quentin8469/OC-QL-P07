import csv




class Action:
    """ Creation de l'objet action"""
    def __init__(self, name, price, profit):
        self.name = name
        self.price = int(price)
        self.profit = int(profit)
        self.gain = self.price*self.profit/100

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Profit: {self.profit}, Gain: {self.gain}'


def data_set_csv(datafile):
    """Open and read the csv file"""
    wallet =[]
    with open(f'data_set/{datafile}.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if float(row[1]) <= 0.0 or float(row[2]) <= 0.0:
	            del(row)
            else:
                wallet.append(Action(row[0], float(row[1]), float(row[2])))

    return wallet


def get_matrix(wallet, max_invest):
    """ Generate a empty matrix"""
    matrix = []
    for largeur in range(0, len(wallet)+1):
        tableau_largeur = []
        for hauteur in range(0, max_invest +1):
            tableau_largeur.append(0)
        matrix.append(tableau_largeur)

    return matrix


def algo_sac_a_dos(wallet, max_invest):
    """"""
    matrice = get_matrix(wallet, max_invest)
    for action in range(1, len(wallet)+1):
        for invest in range(1, max_invest+1):
            if wallet[action-1].price <= invest:
                best_pos = wallet[action-1].profit + matrice[action-1][invest-wallet[action-1].price]
                matrice[action][invest] = max(best_pos, matrice[action-1][invest])
            else:
                matrice[action][invest] = matrice[action-1][invest]
    return matrice


def best_option(wallet, max_invest, matrice):
    """"""

    n = len(wallet)
    optimized_portfolio = []

    while max_invest >= 0 and n >= 0:
        action = wallet[n-1]

        if matrice[n][max_invest] == matrice[n-1][max_invest-action.price] + action.profit:
            print(matrice[n][max_invest])
        #     print(matrice[n][max_invest])
        #     optimized_portfolio.append(e)
        #     k -= e.price
        # n -=1
    return optimized_portfolio


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

    max_invest = 50 #conversion euros en centimes *100
    wallet = data_set_csv(csv_file)
    print("------------sac à dos-------------------")
    print("----------------------------------------------")
    sac_a_dos = algo_sac_a_dos(wallet, max_invest)
    #print('mon resultat', sac_a_dos)
    best_portfolio = best_option(wallet, max_invest, sac_a_dos)
    print('mon resultat final', best_portfolio)
    print("--------------END sac à dos---------------------")
    print("----------------------------------------------")


if __name__ == "__main__":
    """"""
    main()