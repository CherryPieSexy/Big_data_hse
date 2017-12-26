#!/usr/bin/env python
# coding=utf-8
import sys

curr_antiNucleus = None

currFile = None
counter = 0

averagePt = 0.0
counterPt = 0.0

for line in sys.stdin:
    line = line.split('\t')

    if curr_antiNucleus != line[0] or curr_antiNucleus == None: # нашли новый или первый
        if curr_antiNucleus != None: # если новый, то нужно вывести старый
            print(counter, averagePt / (counterPt))
        curr_antiNucleus = line[0]
        currFile = line[1]
        counter = 1
        averagePt = float(line[3])
        counterPt = 1.0

    elif curr_antiNucleus == line[0]: # нашли такой же antiNucleus
        # Посчитаем кол-во уникальных eventFile
        if currFile != line[1]: # нашли новый
            currFile = line[1]
            counter += 1
        # Посчитаем среднее
        averagePt += float(line[3])
        counterPt += 1.0

print(counter, averagePt / (counterPt)) # в конце тоже нужно вывести
