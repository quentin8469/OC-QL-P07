import csv
import time


class Action:
    """ Create the Action object"""
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit
        self.gain = self.price*self.profit/100
        
    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Profit: {self.profit},'\
               f'Gain: {self.gain}'


def data_set_csv(datafile):
    """Open and read the csv file for create a list of action object"""
    wallet =[]
    with open(f'data_set/{datafile}.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if float(row[1]) <= 0.0 or float(row[2]) <= 0.0:
	            del(row)
            else:
                wallet.append(Action(row[0], float(row[1]), float(row[2])))
                
    return wallet


def glouton(wallet, max_invest):
    """ Sorting wallet by profit """
    
    best_combination = []
    total_gain = 0
    total_invest = 0
    wallet_tri = sorted(wallet, key=lambda x:x.profit, reverse=True)
    for wallet in wallet_tri:
        invest = total_invest + wallet.price
        if invest <= max_invest and wallet.gain >0:
            total_invest = invest
            total_gain += wallet.gain
            best_combination.append(wallet.name)

    return f'La meilleure combinaison d\'action est: {best_combination}\n'\
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
    
    max_invest = 500 
    wallet = data_set_csv(csv_file)
    print("------------glouton_one-------------------")
    start_time = time.time()
    algo_glouton = glouton(wallet, max_invest)
    print(algo_glouton)
    end_time = time.time()
    print('Temps d\'execution:' , (end_time - start_time), 'secondes')
    print("--------------END glouton_one---------------------")
    
    
    
if __name__ == "__main__":
    """"""
    main()