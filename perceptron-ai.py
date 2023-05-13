import random

class Perceptron:
    def __init__(self, num_inputs):
        self.weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
        self.bias = random.uniform(-1, 1)

    def predict(self, inputs):
        weighted_sum = sum(w*x for w, x in zip(self.weights, inputs)) + self.bias
        return 1 if weighted_sum >= 0 else 0

    def train(self, training_inputs, labels, learning_rate=0.1, epochs=100):
        for epoch in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                self.weights = [w + learning_rate*error*x for w, x in zip(self.weights, inputs)]
                self.bias += learning_rate*error

# Create a Perceptron object with 2 input nodes
p = Perceptron(2)

# Train the classifiers on OR data
training_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
labels = [0, 1, 1, 1]
p.train(training_inputs, labels)

# Test the classifiers on some new data
print(p.predict((0, 0)))  # Expected output: 0
print(p.predict((0, 1)))  # Expected output: 1
print(p.predict((1, 0)))  # Expected output: 1
print(p.predict((1, 1)))  # Expected output: 1

