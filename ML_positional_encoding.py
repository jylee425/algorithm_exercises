import math

seq_len, model_dim = 3, 8

# input \in (batch_size, seq_len, 1)
# -> output \in (batch_size, seq_len, embedding_dim)

# pt = sin(wk * t) if i = 2k
#    = cos(wk * t) if i = 2k + 1
# wk = 1 / (10000 ** (2k/d))

pos = []
for t in range(seq_len):
    pos_t = []

    for i in range(model_dim):
        k = i // 2
        w_k = 1 / (10000 ** (2 * k / model_dim))

        if i % 2 == 0:
            pos_t.append(math.sin(w_k * t))
        else:
            pos_t.append(math.cos(w_k * t))

    pos.append(pos_t)

print(pos)
