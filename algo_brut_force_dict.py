import csv
from itertools import combinations
import time


def make_dict():
    """Creat a dictionnariy with the data of a csv file"""
    wallet_dict = {}
    
    with open ('data_set/dataset0.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            wallet_dict.update({row[0]:[row[1], row[2]]})
    return wallet_dict


def make_combinations(wallet):
    """ Create all the combination with a wallet"""
    all_combination = []
    for i in range(len(wallet)):
        for combis in (combinations(wallet, i)):
            all_combination.append(combis)
    return all_combination


def find_best_invest(all_combis,max_invest,wallet):
    """ try to find the best combation for the best gain"""
    max_gain = 0
    #total_invest = 0
    best_invest = []
    for combis in all_combis:
        combi_gain = 0
        total_invest = 0
        for combi in combis:
            action_price = int(wallet[combi][0])
            two_year_gain = int(wallet[combi][1])
            action_gain = (action_price * two_year_gain)/100
            combi_gain += action_gain
            total_invest += action_price
            #time.sleep(2)
            #print(combi)
            #print(two_year_gain)
            #print(total_gain)
        if total_invest <= max_invest and combi_gain > max_gain:
            max_gain = combi_gain
            best_invest = combis
            
        else:
            pass
        
        # time.sleep(2)
        # print("Gain max:", combi_gain)
        # print("invest max:", total_invest)
    print(max_gain)
    print(best_invest)
   
def main():
    max_invest = 500
    wallet = make_dict()
    #print(wallet)
    all_combis = make_combinations(wallet)
    #print(all_combis)
    best_invest = find_best_invest(all_combis, max_invest, wallet)
    #print(best_invest)


if __name__ == "__main__":
    main()