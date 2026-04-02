from collections import deque
import numpy as np
import random


class ReplayBuffer:
    def __init__(self, max_size=1000000):
        self.buffer = deque(maxlen=max_size)

    def add(self, transition):
        self.buffer.append(transition)

    def sample(self, batch_size):
        if len(self.buffer) < batch_size:
            return None

        indices = random.sample(range(len(self.buffer)), batch_size)

        return [self.buffer[i] for i in indices]

    def __len__(self):
        return len(self.buffer)

    def clear(self):
        self.buffer.clear()
