import numpy as np
import time
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self):
        self.weigthVectors = np.array([0,0,0])
        self.exampleVector = []
        self.trueLabels = []

    def train(self,examples):
        if len(examples) > 0:
            for example in examples:
                features = example.split(',')
                self.exampleVector.append((1,float(features[0]),float(features[1])))
                self.trueLabels.append(float(features[2]))
            while(True):
                previousWeigthVector = np.copy(self.weigthVectors)
                for exampleIndex in range(len(self.exampleVector)):
                    trueLabel = self.trueLabels[exampleIndex]
                    sfResult = trueLabel * self.stepFunction(exampleIndex)
                    if sfResult <= 0:
                        trueXexample = trueLabel * np.array(self.exampleVector[exampleIndex])
                        np.add(self.weigthVectors, trueXexample, out=self.weigthVectors, casting="unsafe")
                if (previousWeigthVector == self.weigthVectors).all():
                    break
            self.plotExamples()
            self.plotPartialResult()
        else:
            print("No features provided.")

    def stepFunction(self, exampleIndex):
        sumatory = 0
        sumatory = np.dot(self.weigthVectors,self.exampleVector[exampleIndex])
        return sumatory

    def solveEcuation(self):
        w2_vals = range(1, 11)
        print(w2_vals)
        w1_vals = [(self.weigthVectors[0] + (2*w2))/self.weigthVectors[1] for w2 in w2_vals]
        return [w1_vals, w2_vals]

    def plotExamples(self):
        for index,example in enumerate(self.exampleVector):
            if self.trueLabels[index] == 1:
                plt.plot(example[1], example[2], color='blue', marker='o')
            else:
                plt.plot(example[1], example[2], color='red', marker='o')

    def plotPartialResult(self):
        solutions = self.solveEcuation()
        plt.plot(solutions[0],solutions[1])
        plt.show()
        time.sleep(1)
        plt.close()
