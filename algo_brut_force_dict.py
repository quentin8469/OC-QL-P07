import csv
from itertools import combinations
import time


def make_dict(datafile):
    """ Creat a dictionnariy with the data of a csv file """
    wallet_dict = {}
    with open (f'data_set/{datafile}.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            wallet_dict.update({row[0]:[row[1], row[2]]})
    return wallet_dict


def find_best_invest(max_invest,wallet):
    """ try to find the best combation for the best gain """
    max_gain = 0
    all_invest = 0
    best_invest = []
    for i in range(len(wallet)):
        for combis in (combinations(wallet, i)):
            combi_gain = 0
            total_invest = 0
            for combi in combis:
                action_price = float(wallet[combi][0])
                two_year_gain = float(wallet[combi][1])
                action_gain = (action_price * two_year_gain)/100
                combi_gain += action_gain
                total_invest += action_price
            if total_invest <= max_invest and combi_gain > max_gain:
                max_gain = combi_gain
                all_invest = total_invest
                best_invest = combis
            else:
                pass
    return f'La meilleure combinaison d\'action est: {best_invest}\n'\
           f'Pour un gain estimé de: {max_gain} €\n'\
           f'Pour un investissement de:{all_invest} €'

 
def main():
    """ Principal function """
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
    start_time = time.time()
    wallet = make_dict(csv_file)
    best_invest = find_best_invest(max_invest, wallet)
    print(best_invest)
    end_time = time.time()
    print('Temps d\'execution:' , (end_time - start_time), 'secomdes')
    

if __name__ == "__main__":
    """"""
    main()