#Część 1, Wyszukiwanie prostego wzroca 2D
file = open("1000_pattern.txt", "r")

with open("1000_pattern.txt") as txt:
    lines = [line for line in txt]


counter = 0
for x in range(len(lines)-1):
    for y in range(len(lines)-1):
        if(lines[x][y] == 'A' and lines[x][y+1] == 'B' and lines[x][y+2] == 'C'
            and lines[x+1][y] == 'B' and lines[x+2][y] == 'C'):
                #print(x,y)
                counter += 1

print("Found " + str(counter) + " patterns")

#Część 2

import time

file = open("5000_pattern.txt", "r")

with open("5000_pattern.txt") as txt:
    lines = [line for line in txt]

start_time = time.time()
counter = 0
for x in range(len(lines)-2):
    for y in range(len(lines)-2):
        if(lines[x][y] == 'A' and lines[x][y+1] == 'B' and lines[x][y+2] == 'C'
            and lines[x+1][y] == 'B' and lines[x+2][y] == 'C'):
                #print(x,y)
                counter += 1

print("Found " + str(counter) + " patterns")

end_time = time.time()
duration = end_time - start_time

print("Czas dzialania algorytmu wynosi:", duration, "sekundy")