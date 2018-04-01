

class Perceptron:
    def __init__(self):
        self.weigthVectors = [0,0,0]

    def train(self,features):
        if len(features) > 0:
            for feature in features:
        else:
            print("No features provided.")

    def stepFunction(self, features):
        sumatory = 0
        for i in range(len(self.weigthVectors)+1):
            sumatory = self.weigthVectors[i]
