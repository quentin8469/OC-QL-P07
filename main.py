import algo_brut_force_dict
import algo_optimized

def main():
    """"""
    algo = '0'
    while algo != '3':
        print("----------------------------------------------")
        print("               AlgoInvestTrade                ")
        print("----------------------------------------------")
        print("1:Brute_Force        2:Optimisé         3:Exit")
        algo = input("Entrez votre choix et appuyez sur entrée: ")
        print("----------------------------------------------")
        if algo == '1':
            print('Le programme brut force vient de débuter')
            algo_brut_force_dict.main()
        elif algo == '2':
            print('Le programme optimized vient de débuter')
            algo_optimized.main()
        elif algo == '3':
            exit

if __name__ == "__main__":
    """"""
    main()