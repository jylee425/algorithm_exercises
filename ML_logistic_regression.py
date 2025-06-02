import numpy as np

# dataset
X_train, X_test, Y_train, Y_test
N, D_in = X_train.shape
_, D_out = Y_train.shape


# model y = sigmoid ( wx + b )
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def BCELoss(y_label, y_pred):
    return -y_label * np.log(y_pred + 1e-9) - (1 - y_label) * np.log(1 - y_pred + 1e-9)


W = np.random.rand(D_in, 1)
b = np.random.rand(1)

# optimization
lr = 1e-3
epochs = 10000

for e in range(epochs):
    pred = sigmoid(X_train.dot(W) + b)

    # gradient computation
    dLdW = (X_train.T.dot(Y_train - pred)) / N
    dLdb = np.mean(Y_train - pred)

    # update
    W -= lr * dLdW
    b -= lr * dLdb

    if e % 1000 == 0:
        loss = -np.mean(BCELoss(Y_train, pred))
        print(f"Epoch {e}: Train BCE Loss = {loss:.4f}")
