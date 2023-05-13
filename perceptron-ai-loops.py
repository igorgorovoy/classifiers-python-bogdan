import random

def dot_product(x, w):
    """
    Computes the dot product between the input vector x and the weight vector w.
    """
    return sum(xi * wi for xi, wi in zip(x, w))

def predict(x, w):
    """
    Computes the prediction (0 or 1) for the input vector x using the weight vector w.
    """
    return 1 if dot_product(x, w) >= 0 else 0

def train_perceptron(X, y, learning_rate=0.1, num_epochs=100):
    """
    Trains a classifiers model on the input data X and labels y.
    """
    num_features = len(X[0])
    print("num_features is " +str(num_features))
    w = [random.random() for i in range(num_features)]
    print("Weights is " + str(w))
    for epoch in range(num_epochs):
        for xi, yi in zip(X, y):
            predicted = predict(xi, w)
            error = yi - predicted
            w = [wi + learning_rate * error * xi[i] for i, wi in enumerate(w)]
    return w

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 0, 0, 1]

w = train_perceptron(X, y)

for xi, yi in zip(X, y):
    predicted = predict(xi, w)
    print(xi, predicted, yi)
