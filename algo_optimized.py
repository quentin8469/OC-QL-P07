import csv
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
	        wallet.append(Action(row[0], float(row[1]), float(row[2])))
    return wallet


def glouton(wallet, max_invest):
    """ try to find a good invest """
    #trier les objets action par gain possible
    wallet_tri = sorted(wallet, key=lambda x:x.gain, reverse=True)
    for tes in wallet_tri:
        print('test tri glouton:', tes.name , tes.price, tes.gain)


def main():
    """"""
    max_invest = 500
    csv_file = input('dataset0 ou dataset1_Python+P7 ou dataset2_Python+P7 :' )
    wallet = data_set_csv(csv_file)
    opti_invest = glouton(wallet, max_invest)

if __name__ == "__main__":
    """"""
    main()