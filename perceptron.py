import numpy as np

class Perceptron:
    def __init__(self):
        self.weigthVectors = [0,0,0]
        self.exampleVector = ()
        self.trueLabels = []

    def train(self,examples):
        if len(examples) > 0:
            for example in examples:
                features = example.split(',')
                self.exampleVector.append((1,features[0],features[1]))
                self.trueLabels.append(features[2])
            previousWeigthVector = [0,0,0]
            while(True):
                for exampleIndex in range(len(self.exampleVector)+1):
                    trueLabel = self.trueLabels[exampleIndex]
                    sfResult = trueLabel * self.stepFunction(exampleIndex)
                    if sfResult <= 0:
                        previousWeigthVector = list(self.weigthVectors)
                        for weightVector in self.weigthVectors:
                            weightVector += trueLabel * np.array(self.exampleVector[exampleIndex])
                if previousWeigthVector != self.weigthVectors:
                    break
        else:
            print("No features provided.")

    def stepFunction(self, exampleIndex):
        sumatory = 0
        for featureIndex in range(len(self.weigthVectors)+1):
            feature = self.exampleVector[exampleIndex][featureIndex]
            sumatory += self.weigthVectors[featureIndex] * feature
        return sumatory
