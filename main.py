import random, time


def pause(num):
    time.sleep(num)


def line(string):
    print(string)
    time.sleep(1)


line("LOADING...")
line("LOADED")
line("What do you wish to label the data?")
outputName = input(">>> ")
with open(f"{outputName}.txt", 'x') as output:
    output.close()

with open(f"{outputName}_RAW.txt", 'x') as output:
    output.close()

templateOrganism = {"MR": [1, 3],
                    "MS": [1,  3],
                    "L": [3, 7],
                    "LS": [1, 5],
                    "GP": [2, 4],
                    "F": [1, 50],
                    "MaxTemp": [5, 15],
                    "MinTemp": [(0-5), (0-15)]}