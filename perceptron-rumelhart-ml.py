import numpy as np

# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the forward propagation step
def forward(x, weights1, bias1, weights2, bias2):
    hidden_output = sigmoid(np.dot(x, weights1) + bias1)
    output = sigmoid(np.dot(hidden_output, weights2) + bias2)
    return output, hidden_output

# Define the backpropagation step
def backward(x, y, output, hidden_output, weights1, bias1, weights2, bias2):
    error = y - output
    delta_output = error * output * (1 - output)
    delta_hidden = np.dot(delta_output, weights2.T) * hidden_output * (1 - hidden_output)

    weights2 += np.dot(hidden_output.T, delta_output)
    bias2 += np.sum(delta_output, axis=0)

    weights1 += np.dot(x.T, delta_hidden)
    bias1 += np.sum(delta_hidden, axis=0)

# Initialize the parameters of the network
input_size = 2
hidden_size = 16
output_size = 1

weights1 = np.random.randn(input_size, hidden_size)
bias1 = np.random.randn(hidden_size)

weights2 = np.random.randn(hidden_size, output_size)
bias2 = np.random.randn(output_size)

# Train the network on some data
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

for i in range(10000):
    output, hidden_output = forward(X, weights1, bias1, weights2, bias2)
    backward(X, y, output, hidden_output, weights1, bias1, weights2, bias2)

# Test the network on some new data
new_data = np.array([[0,1], [1,0]])
predictions, _ = forward(new_data, weights1, bias1, weights2, bias2)
print(predictions)
