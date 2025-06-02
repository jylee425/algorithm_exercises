import torch
import torch.nn.functional as F

mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1).bool()


def scaled_dot_product_attention(q, k, v, mask=None):
    """
    softmax(q @ k^T / sqrt(d_k)) @ v
    """
    d_k = k.size(-1)

    scores = torch.matmul(q, k.transpose(-2, -1))
    scores = scores / d_k**0.5

    if mask is not None:
        scores = scores.masked_fill(mask, float("-inf"))

    attn = F.softmax(scores, dim=-1)
    return torch.matmul(attn, v)
