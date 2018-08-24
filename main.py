import sys
import csv

from perceptron import Perceptron

input_file = sys.argv[1]
output_file = sys.argv[2]
features = []

with open(input_file, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        features += row

perceptron = Perceptron(output_file)
perceptron.train(features)
