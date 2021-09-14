import csv
# import os
# import itertools

def data_set_csv():
    """ Open and read the csv file"""
    with open('data_set/dataset0.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
	        print (row)


def main():
    """"""
    # ouvrir mon fichier dataset.csv
    # lire les datas de mon fichier
    # calculer les gains de chaque actions sur 2 ans ((coût*benef)/100)
    # enregistrer les gains pour chaque actions
    # tester chaques combinaisons possible d'action pour un investisement max de 500€ et une rentabilité maximale
    # afficher la reponse
    pass

if __name__ == "__main__":
    print('open')
    data_set_csv()