# understing basics steps of nn
# article: https://www.kdnuggets.com/2019/11/build-artificial-neural-network-scratch-part-1.html

import numpy as np

#Independent variables
input_set = np.array([[0,1,0],
                      [0,0,1],
                      [1,0,0],
                      [1,1,0],
                      [1,1,1],
                      [0,1,1],
                      [0,1,0]])#Dependent variable
labels = np.array([[1,
                    0,
                    0,
                    1,
                    1,
                    0,
                    1]])
labels = labels.reshape(7,1) #to convert labels to vector

# Define Hyperparameters
np.random.seed(42)
weights = np.random.rand(3,1)
bias = np.random.rand(1)
lr = 0.05 #learning rate

# Define Activation Function and it’s derivative: Our activation function is the sigmoid function.
def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x)*(1-sigmoid(x))

# train
for epoch in range(25000):
    inputs = input_set
    XW = np.dot(inputs, weights)+ bias # step-1 of Feedforward phase
    z = sigmoid(XW) # Step-2 of Feedforward phase
    error = z - labels # first step of the backpropagation is to find the error
    print(error.sum())
    dcost = error
    dpred = sigmoid_derivative(z)
    z_del = dcost * dpred
    inputs = input_set.T
    weights = weights - lr*np.dot(inputs, z_del)
    
    for num in z_del:
        bias = bias - lr*num


# make predictions
single_pt = np.array([1,0,0])
result = sigmoid(np.dot(single_pt, weights) + bias)
print(result)