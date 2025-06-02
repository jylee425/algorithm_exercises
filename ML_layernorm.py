import torch
import torch.nn as nn


class LayerNorm(nn.Module):
    """
    layernorm = ((x - mean(x)) / std(x)) * gamma + beta
    """

    def __init__(self, normalized_shape):
        super(LayerNorm, self).__init__()
        self.beta = nn.Parameter(torch.zeros(normalized_shape))
        self.gamma = nn.Parameter(torch.ones(normalized_shape))

    def forward(self, x):
        mean = torch.mean(x, dim=-1, keepdims=True)
        var = torch.var(x, dim=-1, keepdims=True, unbiased=False)

        x_norm = (x - mean) / torch.sqrt(var + self.eps)
        return self.beta + self.gamma * x_norm
