#problem plecakowy, algorytmem aproksymacyjnym

import time
import numpy as np


def sprawdz_umieszczenie(x, y, plecak):
    for x_start in range(len(plecak) - x + 1):
        for y_start in range(len(plecak) - y + 1):
            pasuje = True
            for x_iter in range(x):
                for y_iter in range(y):
                    if plecak[x_start + x_iter][y_start + y_iter]:
                        pasuje = False
                        break
                if not pasuje:
                    break
            if pasuje:
                return (x_start, y_start, False)

    for x_start in range(len(plecak) - x + 1):
        for y_start in range(len(plecak) - y + 1):
            pasuje = True
            for x_iter in range(x):
                for y_iter in range(y):
                    if plecak[y_start + y_iter][x_start + x_iter]:
                        pasuje = False
                        break
                if not pasuje:
                    break
            if pasuje:
                return (x_start, y_start, True)

    return False


if __name__ == "__main__":
    for rozmiar in ['20', '100', '500', '1000']:
        start = time.time()
        with open('packages' + rozmiar + '.txt') as txt:
            przedmioty = [line.split(",") for line in txt]

        del (przedmioty[0])
        del (przedmioty[0])

        for przedmiot in przedmioty:
            przedmiot[-1] = przedmiot[-1].strip()

        przedmioty = [[int(j) for j in i] for i in przedmioty]

        for przedmiot in przedmioty:
            przedmiot.append(przedmiot[3] / (przedmiot[1] * przedmiot[2]))

        przedmioty.sort(key=lambda x: -x[4])

        plecak = np.zeros((int(rozmiar), int(rozmiar)), dtype=int)
        wartosc = 0
        iteracja = 0

        for przedmiot in przedmioty:
            pasuje = sprawdz_umieszczenie(przedmiot[1], przedmiot[2], plecak)
            if pasuje:
                iteracja += 1

                if pasuje[2]:
                    for x in range(pasuje[0], przedmiot[1] + pasuje[0]):
                        for y in range(pasuje[1], przedmiot[2] + pasuje[1]):
                            plecak[y][x] = iteracja

                else:
                    for x in range(pasuje[0], przedmiot[1] + pasuje[0]):
                        for y in range(pasuje[1], przedmiot[2] + pasuje[1]):
                            plecak[x][y] = iteracja

                wartosc += przedmiot[3]

        print(plecak)
        print("chciwy, " + str(rozmiar) + ", " + str(time.time() - start))
        print("zebrana wartosc:", wartosc)

        # wartosc wszystkich przedmiotow
        suma = 0
        for przedmiot in przedmioty:
            suma += przedmiot[3]

        print("maksymalna mozliwa wartosc:", suma)
