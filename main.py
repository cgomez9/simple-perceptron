import sys
import csv

from perceptron import Perceptron

input_file = sys.argv[1]
features = []

with open(input_file, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        features += row

perceptron = Perceptron()
perceptron.train(features)
