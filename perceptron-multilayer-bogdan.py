import numpy as np

IN = np.array([1.0, 2.4, -1.2])
IN2 = np.array([])

W1 = np.array([[0.1, 0.1, 0.1],
               [0.1, 0.1, 0.1]])

W2 = np.array([[0.1, 0.1],
               [0.1, 0.1],
               [0.1, 0.1]])

W1_prev = np.array([[0.1, 0.1, 0.1],
                    [0.1, 0.1, 0.1]])

W2_prev = np.array([[0.1, 0.1],
                    [0.1, 0.1],
                    [0.1, 0.1]])

TARG = np.array([1.0, 2.4, -1.2])
BIAS = 0
ERR = np.array([])
ERR_prev = np.array([99, 99])


# for i in range(10000):
#     IN2 = np.dot(W1, IN) + BIAS
#     OUT = np.dot(W2, IN2) + BIAS
#
#     ERR = np.subtract(TARG, OUT)
#     print(ERR)
#     print(IN)
#
#     if np.sum(ERR) < np.sum(ERR_prev):
#         ERR_prev = ERR
#         W1_prev = W1
#         W2_prev = W2
#     else:
#         W1 = W1_prev
#         W2 = W2_prev
#
#     W1 += 0.0004 * np.outer(ERR, IN)
#     W2 += 0.0004 * np.outer(ERR, IN2)
#
#     print("Weights: ", W1, W2)
#     print("Target: ", TARG)
#     print("Outputs: ", OUT)
#     print("Errors: ", ERR)
# print("Best: ", W1_prev, W2_prev)