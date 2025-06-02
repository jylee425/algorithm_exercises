import numpy as np

# dataset
X_train, X_test, Y_train, Y_test
N, D = X_train.shape
_, C = Y_train.shape


# model
# y = softmax( Wx + b )
def softmax(logits, axis=-1):
    logits_max = np.max(logits, axis=axis, keepdims=True)
    exp_logits = np.exp(logits - logits_max)
    return exp_logits / np.sum(exp_logits, axis=axis, keepdims=True)


W = np.random.rand(D, C)
b = np.random.rand(1, C)


# loss
# L = - \sum log(pred)
def cross_entropy_loss(pred, label):
    N = pred.shape[0]
    log_prob = np.log(pred[np.arange(N), label] + 1e-9)
    return -1 * np.sum(log_prob, axis=1) / N


# optimiation
lr = 1e-3
epochs = 1000
for e in range(epochs):
    logits = X_train.dot(W) + b
    prob = softmax(logits)
    loss = cross_entropy_loss(pred, Y_train)

    # gradients
    # dW = X^T * (y^ - y)
    # db = (y^ - y)
    dlogits = prob.copy()
    dlogits[np.arange(N), Y_train] -= 1
    dW = X_train.T.dot(dlogits) / N
    db = np.mean(dlogits, keepdims=True)

    W -= lr * dW
    b -= lr * db
