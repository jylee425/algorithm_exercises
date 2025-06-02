import torch
import torch.nn as nn
import torch.nn.functional as F

# Dataset
X_train, X_test, Y_train, Y_test
N, D_in = X_train.shape
M, D_out = X_test.shape


# model
class MLP(nn.Module):
    def __init__(self, input_dim=28 * 28, hidden_dim=32, output_dim=10):
        super(MLP, self).__init__()

        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)
        self.activation = nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)
        x = self.activation(x)
        x = self.fc2(x)
        return x


model = MLP(input_dim=D_in, output_dim=D_out)

# optimization
lr = 1e-3
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=lr)

# training loop
epochs = 1000
for e in range(epochs):
    pred = model(X_train)
    loss = criterion(pred, Y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if e % 1000 == 0:
        print(loss)
