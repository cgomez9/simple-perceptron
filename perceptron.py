import numpy as np
import time
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self):
        self.weigth_vectors = np.array([0,0,0])
        self.example_vector = []
        self.true_labels = []

    def train(self,examples):
        if len(examples) > 0:
            for example in examples:
                features = example.split(',')
                self.example_vector.append((1,float(features[0]),float(features[1])))
                self.true_labels.append(float(features[2]))
            while(True):
                previous_weigth_vector = np.copy(self.weigth_vectors)
                for example_index in range(len(self.example_vector)):
                    true_label = self.true_labels[example_index]
                    sf_result = true_label * self.step_function(example_index)
                    if sf_result <= 0:
                        true_x_example = true_label * np.array(self.example_vector[example_index])
                        np.add(self.weigth_vectors, true_x_example, out=self.weigth_vectors, casting="unsafe")
                if (previous_weigth_vector == self.weigth_vectors).all():
                    break
            self.plot_examples()
            self.plot_partial_results()
        else:
            print("No features provided.")

    def step_function(self, example_index):
        sumatory = 0
        sumatory = np.dot(self.weigth_vectors,self.example_vector[example_index])
        return sumatory

    def solve_ecuation(self):
        w2_vals = range(1, 11)
        w1_vals = [(self.weigth_vectors[0] + (2*w2))/self.weigth_vectors[1] for w2 in w2_vals]
        return [w1_vals, w2_vals]

    def plot_examples(self):
        for index,example in enumerate(self.example_vector):
            if self.true_labels[index] == 1:
                plt.plot(example[1], example[2], color='blue', marker='o')
            else:
                plt.plot(example[1], example[2], color='red', marker='o')

    def plot_partial_results(self):
        solutions = self.solve_ecuation()
        plt.plot(solutions[0],solutions[1])
        plt.show()
        time.sleep(1)
        plt.close()
