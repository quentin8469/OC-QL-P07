import csv
from itertools import combinations


def make_dict():
    wallet_dict = {}
    with open ('data_set/dataset1_Python+P7.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            #wallet_dict_csv = {row[0]:row[1]}
            wallet_dict.update({row[0]:[row[1], row[2]]})
    return wallet_dict


def main():
    wallet = make_dict()
    print(wallet)


if __name__ == "__main__":
    main()