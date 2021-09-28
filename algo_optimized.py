import csv
from itertools import combinations
from os import name



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
    #création de ma matrice:
        #je veux crée un tableau de largeur 'max invest' et de hauteur 'nombre d'actions'
    #retourne un matrice avec que des zéros   
    
    
    #une fois ma matrice crée:
    #pour ma hauteur comprise entre 0 et 'nombre d'actions'
        #pour ma largeur comprise entre 0 et max_invest:
            #si le prix de mon action est inferieur ou égal à ma largeur ( largeur = au niveau d'investissement de ma boucle ):
                    #mon meilleur bénéfice pour l'investissement de ma boucle = bénéfice de l'action additionné au bénéfice de l'action précédente que je peux acheter avec le reste de l'investissement
                    #je vais comparer le bénéfice actuel avec le bénéfice possible précèdent pour le même investissement et j'insert le meilleurs résultat dans mon tableau.  
            
            #si mon prix est strictement supérieur:
                #je prend la valeur précédente de l'investissement donné et je l'ajoute a mon tableau
                
    matrice = get_matrix(wallet, max_invest)
    
    # print('matrice vide', matrice)
    # for action in range(1, len(wallet) + 1):
    #      #print('action',action)
    #      for invest in range(1, max_invest + 1):
    #         #print('invest', invest)
    #         if wallet[action-1].price <= invest:
    #             max_profit = wallet[action-1].profit + matrice[invest][wallet[action-1].profit]
    #             print('max_profit', max_profit) 
    #             autre_profit = matrice[invest][wallet[action-1].profit]
    #             print('autre_profit', autre_profit)
    #             matrice[invest][action] = max(matrice[invest-1][action], max_profit)
    #             print(matrice[invest][action])
    #         else:
    #             matrice[invest][action] = matrice[invest-1][action] 
    #             print('matrice[invest][action]', matrice[invest][action])
    
    print('matrice vide', matrice) 
    for action in range(1, len(wallet)+1):
        print('action',action)
        for invest in range(1, max_invest+1):
            print('invest', invest)
            if wallet[action-1].price <= invest:
                best_pos = wallet[action-1].profit + matrice[action-1][invest-wallet[action-1].price]
                print('wallet[action-1].profit', wallet[action-1].profit)
                print('matrice[action-1][invest-wallet[action-1].price]', matrice[action-1][invest-wallet[action-1].price])
                print('best_pos', best_pos) 
                matrice[action][invest] = max(best_pos, matrice[action-1][invest])
                print(matrice[action][invest])
            else:
                matrice[action][invest] = matrice[action-1][invest]
    return matrice
    
    

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
    #print(len(sac_a_dos))
    print('mon resultat', sac_a_dos)
    # matrix= get_matrix(wallet, max_invest)
    # print(matrix)
    print("--------------END sac à dos---------------------")
    print("----------------------------------------------")


if __name__ == "__main__":
    """"""
    main()