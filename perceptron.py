

class Perceptron:
    def __init__(self):
        self.weigthVectors = [0,0,0]
        self.exampleVector = []

    def train(self,examples):
        if len(examples) > 0:
            for example in examples:
                features = example.split(',')
                self.exampleVector.append((features[0],features[1], features[2]))
            previousWeigthVector = [0,0,0]
            while(True):
                for exampleIndex in range(len(self.exampleVector)+1):
                    trueLabel = self.exampleVector[exampleIndex][2]
                    sfResult = trueLabel * self.stepFunction(exampleIndex)
                    if sfResult <= 0:
                        for weightVector in self.weigthVectors:
                            weightVector += trueLabel * 
                        previousWeigthVector = 


        else:
            print("No features provided.")

    def stepFunction(self, exampleIndex):
        sumatory = 0
        for featureIndex in range(len(self.weigthVectors)+1):
            feature = self.exampleVector[exampleIndex][featureIndex]
            sumatory += self.weigthVectors[featureIndex] * feature
        return sumatory
