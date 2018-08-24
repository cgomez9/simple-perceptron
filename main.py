import sys
import csv

from perceptron import Perceptron

inputFile = sys.argv[1]
features = []

with open(inputFile, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        features += row

perceptron = Perceptron()
perceptron.train(features)
