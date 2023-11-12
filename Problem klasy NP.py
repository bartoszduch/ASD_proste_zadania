#Część1, problem komiwojażera
#Kod wykorzystuje współrzędne kartezjańskie
#100 miast zapisane w pliku TSP.txt
from random import shuffle
from math import sqrt

if __name__ == "__main__":
    with open('TSP.txt') as txt:
        miasta = [line.split() for line in txt]

    shuffle(miasta)

    poprzednie_miasto = [0, 0, 0]
    odleglosc = 0

    for miasto in miasta:
        odleglosc += sqrt((float(miasto[1]) - float(poprzednie_miasto[1])) ** 2 + (
                    float(miasto[2]) - float(poprzednie_miasto[2])) ** 2)
        poprzednie_miasto = miasto

    odleglosc += sqrt((float(miasta[0][1]) - float(poprzednie_miasto[1])) ** 2 + (
                float(miasta[0][2]) - float(poprzednie_miasto[2])) ** 2)

    for miasto in miasta:
        print(miasto[0])

    print(miasta[0][0])
    print(odleglosc)

#Częśc 2
import numpy as np
from math import inf, sqrt


if __name__ == "__main__":
    with open('TSP.txt') as txt:
        miasta = [line.split() for line in txt]

    n_miasta = len(miasta)

    adj_matrix = np.zeros([n_miasta, n_miasta])
    for x in range(n_miasta):
        for y in range(n_miasta):
            adj_matrix[x][y] = sqrt((float(miasta[x][1]) - float(miasta[y][1])) ** 2
                                   + (float(miasta[x][2]) - float(miasta[y][2])) ** 2)

    scieszka = [0]
    dlugosc = 0
    for i in range(n_miasta - 1):
        minimum = inf
        for j in range(n_miasta):
            if j not in scieszka and adj_matrix[scieszka[-1]][j] < minimum:
                minimum = adj_matrix[scieszka[-1]][j]
                min_j = j

        dlugosc += minimum
        scieszka.append(min_j)

    dlugosc += adj_matrix[scieszka[-1]][0]
    scieszka.append(0)

    print("Path:", scieszka)
    print("Length:", dlugosc)