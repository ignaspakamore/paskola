from calculator import Calculate
import tableprint as tp
import numpy as np
import csv
from ascII import *
import pickle as pkl
import pandas as pd
import os
import datetime




def main(history):
    main_meniu()
    inpt = input()

    if inpt == "1":

        amount = int(input("Paskolos suma: "))
        period = int(input("Terminas: "))
        intrate = int(input("Palukanos: "))

        dt = datetime.datetime.now()
        str_dt = dt.strftime("%y-%m-%d %H:%M")

        history.append([amount, period, intrate, str_dt])

        info(amount, period, intrate)

        meniu2()
        cont_inpt = input()
        if cont_inpt == '1':
            c = Calculate(amount, period, intrate)
            data = c.loan_pars()[1]
            matrix = np.array(data).T
            headers = ['Mėn. Nr.', 'Grąžintina dalis', 'Likutis','Palūkanos', 'Grazintina suma']
            tbl()
            tp.table(matrix, headers)

            cont_inpt2 = input("Issaugoti grafika .csv file?(t/n): ")
            if cont_inpt2 == 't':
                graph = pd.DataFrame(matrix, columns=['Mėn. Nr.', 'Grąžintina dalis',
                                                      'Likutis','Palūkanos', 'Grazintina suma'])
                idx = len(history)
                graph.to_csv(f'linijinis_mokejimo_grafikas_{idx}.csv')
                dir = os.getcwd()
                print(f'Filas issaugotas: {dir}+/linijinis_mokejimo_grafikas.csv')

            elif cont_inpt2 == 'n':
                pass

        elif cont_inpt == '2':
            godbye()
            exit()
        else:
            print('Pasirinkite [1] arb [2]')

    elif inpt == '2':

        idx = [ [i] for i in range(len(history))]
        hst_matrix = np.array(history)
        hst_matrix = np.append(hst_matrix, idx, axis=1)

        hstr()
        headers = ['Paskolos suma', 'Terminas', 'Palukanos', 'Data', 'Paieskos ndeksas']
        tp.table(hst_matrix, headers)

        print('[1] Pasirinkti indeksa [2] Pagrindinis Meniu, [3] Baigti darba')

        inpt3 = input()

        if inpt3 == '1':
            inpt_idx = int(input('Iveskite indeksa: '))
            headers = ['Paskolos suma', 'Terminas', 'Palukanos', 'Data', 'Paieskos indeksas']

            tp.table(hst_matrix[inpt_idx:], headers)
            print('[1] Pateikti pasirinkta paskolos mokejimo grafika [2] Pagrindinis meniu [3] Baigti darba')

            inpt4 = input()

            if inpt4 == '1':

                print(hst_matrix[inpt_idx][0], hst_matrix[inpt_idx][1], hst_matrix[inpt_idx][2])


                c = Calculate(hst_matrix[inpt_idx][0], hst_matrix[inpt_idx][1], hst_matrix[inpt_idx][2])
                data = c.loan_pars()[1]
                matrix = np.array(data).T
                headers = ['Mėn. Nr.', 'Grąžintina dalis', 'Likutis', 'Palūkanos', 'Grazintina suma']
                tbl()
                tp.table(matrix, headers)
            elif inpt4 == '2':
                pass

            elif inpt4 == '3':
                godbye()
                exit()
        elif inpt3 == '2':
            pass
        elif inpt3 == '3':
            godbye()
            exit()



    elif inpt == '3':
        godbye()
        exit()
    else:
        print(print('Pasirinkite [1] [2] arba [3]'))


if __name__ == "__main__":
    header()
    history = []
    f = open('history.pkl', 'ab')

    

    while True:
        main(history)




















