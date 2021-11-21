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
                    "MinTemp": [(5), (15)]}

print("Generating population...")
population = []
while len(population) < 100:
    toad1 = {"MR": random.randint(templateOrganism["MR"][0], templateOrganism["MR"][1]),
                        "MS": random.randint(templateOrganism["MS"][0], templateOrganism["MS"][1]),
                        "L": random.randint(templateOrganism["L"][0], templateOrganism["L"][1]),
                        "LS": random.randint(templateOrganism["LS"][0], templateOrganism["LS"][1]),
                        "GP": random.randint(templateOrganism["GP"][0], templateOrganism["GP"][1]),
                        "F": random.randint(templateOrganism["F"][0], templateOrganism["F"][1]),
                        "MaxTemp": random.randint(templateOrganism["MaxTemp"][0], templateOrganism["MaxTemp"][1]),
                        "MinTemp": 0-random.randint(templateOrganism["MinTemp"][0], templateOrganism["MinTemp"][1])}
    population.append(toad1)
    print(f"Organism {len(population)} generated")

with open(f"{outputName}_seed_population.txt", 'x') as output:
    for i in range(len(population)):
        output.write(str(population[i])+"\n")
    output.close()

maxTempAverage = 0
for i in range(len(population)):
    maxTempAverage += population[i]["MaxTemp"]

maxTempAverage = maxTempAverage/100

minTempAverage = 0
for i in range(len(population)):
    minTempAverage += population[i]["MinTemp"]

minTempAverage = minTempAverage/100
medianTemp = maxTempAverage+minTempAverage
medianTemp = medianTemp/2
print(medianTemp)