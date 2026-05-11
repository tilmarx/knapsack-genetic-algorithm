def selection(list, bin, rest):
    count = 0
    sel = 0
    temp_sel = 0
    lowest_sel_index = 0
    index1 = 0
    index2 = 0
    while count < len(bin)-rest:  # rest Anordnungen sollen übrig bleiben
        while index1 < len(bin):  # jede übrige Anordnung
            for thing in list:  # für jeden Gegenstand
                temp_sel += thing[0]*bin[index1][index2] # Wert der Anordnung wird aufaddiert
                index2 += 1
            if index1 == 0:
                sel = temp_sel
            elif temp_sel < sel:
                sel = temp_sel
                lowest_sel_index = index1
            temp_sel = 0
            index2 = 0
            index1 += 1
        bin.pop(lowest_sel_index)
        lowest_sel_index = 0
        index1 = 0
        count += 1


def newgen(bin, list, capacity, amount, rest):
    temp_bin = []
    for i in range(rest):  # für jede Anordnung der Gegenstände
        temp_capacity = -1
        while temp_capacity < 0:  # bis eine Kreuzung gefunden wurde, die die Kapazität nicht übersteigt
            temp_capacity = capacity
            a = randint(0, amount)  # a gibt die Schnittstelle der Kreuzung an
            temp_bin.extend(bin[i][:a])
            temp_bin.extend(bin[i+1][a:])
            for number in range(amount):
                if temp_bin[number] == 1:
                    temp_capacity -= list[number][1]
            if temp_capacity >= 0:
                bin.append(temp_bin.copy())
            temp_bin = []


def mutation(bin, list, capacity, amount, rest):
    temp_bin = []
    for i in range(rest*2):  # jede Anordnung mutiert
        temp_capacity = -1
        while temp_capacity < 0:
            temp_capacity = capacity
            temp_bin = []
            temp_bin.extend(bin[i])
            for number in temp_bin:
                if randint(0,5) == 1:  #20% Chance auf Mutation
                    number = (number-1)*(-1)
            for number in range(amount):
                if temp_bin[number] == 1:
                    temp_capacity -= list[number][1]
            if temp_capacity >= 0:
                bin.append(temp_bin.copy())


from random import randint
things = []
rucksack = []
capacity = int(input('Gib die Kapazität des Rucksacks an: '))
number_things = int(input('Gib die Anzahl der Gegenstände an: '))
highest_value = int(input('Gib den maximalen Wert eines Gegenstandes an (in natürlichen Zahlen): '))
lowest_value = 0
highest_weight = int(input('Gib das maximale Gewicht eines Gegenstandes an (in natürlichen Zahlen): '))
lowest_weight = 1
number_generation = int(input('Gib die Anzahl der erzeugten Generationen an: '))
value = 0
temp_capacity = 0
bin = []
temp_bin = []
rest = 30
n = 0
generation = 0
start_generation = number_things*2
count1 = 0
count2 = 0

# Erzeugung der Gegenstände und ersten Generation
while count1 < number_things:
    things.append((randint(lowest_value, highest_value), randint(lowest_weight, highest_weight)))  # (Wert, Gewicht)
    count1 += 1
count1 = 0
for thing in things:
    temp_capacity += thing[1]
if temp_capacity < capacity:
    while count1 < number_things:
        temp_bin.append(1)
        count1 += 1
    bin.append(temp_bin)
else:
    while count1 < start_generation:
        temp_capacity = capacity
        temp_bin = []
        while count2 < number_things:
            temp_bin.append(0)
            count2 += 1
        count2 = 0
        while temp_capacity >= 0:
            n = randint(0, number_things-1)
            if temp_bin[n] == 0:
                temp_capacity -= things[n][1]
                temp_bin[n] = 1
        temp_capacity += things[n][1]
        temp_bin[n] = 0
        bin.append(temp_bin.copy())
        count1 += 1

    temp_capacity = 0
    n = 0
    while generation < number_generation:
        selection(things, bin, rest)
        newgen(bin, things, capacity, number_things, rest)
        mutation(bin, things, capacity, number_things, rest)
        generation += 1
        print(generation)
    selection(things, bin, 1)

for number in range(number_things):
    if bin[0][number] == 1:
        temp_capacity += things[number][1]
        value += things[number][0]
        rucksack.append(things[number])
print('Das sind alle zur Verfügung stehenden Gegenstände:',things)
print('Der Rucksack hat eine Kapazität von '+str(capacity)+'kg. Davon werden '+str(temp_capacity/capacity*100)+'% genutzt.')
print('Der erzielte Wert liegt bei '+str(value)+'€.')
print('Die mitgenommenen Gegenstände sind Folgende: ',rucksack)
