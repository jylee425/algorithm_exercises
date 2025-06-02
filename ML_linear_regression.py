import numpy as np

# dataset
X_train, X_test, Y_train, Y_test
N, D_in = X_train.shape
_, D_out = Y_train.shape

# model y = \theta x
W = np.random.rand(D_in + 1, D_out)
X_train_ = np.concatenate([X_train, np.ones(N, 1)], axis=-1)  # consider bias term
X_test_ = np.concatenate([X_test, np.ones(M, 1)], axis=-1)  # consider bias term

# optimization
lr = 1e-3
epochs = 1000
for e in range(epochs):
    pred = X_train_.dot(W)
    # loss = (Y_train - pred) ** 2
    dLdw = -2 * X_train_.T.dot(Y_train - pred) / N
    W -= lr * dLdw  # gradient descent

    if e % 1000 == 0:
        pred = X_test_.dot(W)
        loss = np.mean((Y_test - pred) ** 2)
        print(loss)
