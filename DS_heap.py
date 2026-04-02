"""
0
1            2
3     4      5       6
7  8  9  10  11  12  13 14

parent_idx = (idx - 1)// 2

"""


class HeapQ:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

        self._sift_up(len(self.data) - 1)

        return

    def pop(self):
        if len(self.data) == 0:
            return None

        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        val = self.data.pop()

        if len(self.data) > 0:
            self._sift_down(0)

        return val

    def _sift_up(self, curr_idx):
        while True:
            if curr_idx <= 0:
                break

            parent_idx = (curr_idx - 1) // 2

            if self.data[parent_idx] <= self.data[curr_idx]:
                break

            self.data[parent_idx], self.data[curr_idx] = (
                self.data[curr_idx],
                self.data[parent_idx],
            )
            curr_idx = parent_idx

    def _sift_down(self, curr_idx):
        n = len(self.data)

        while True:
            left_child, right_child = 2 * curr_idx + 1, 2 * curr_idx + 2
            smallest = curr_idx

            if left_child < n and self.data[left_child] < self.data[smallest]:
                smallest = left_child

            if right_child < n and self.data[right_child] < self.data[smallest]:
                smallest = right_child

            if curr_idx == smallest:
                break
            self.data[curr_idx], self.data[smallest] = (
                self.data[smallest],
                self.data[curr_idx],
            )
            curr_idx = smallest

    def peek(self):
        return self.data[0] if len(self.data) > 0 else None


h = HeapQ()
for x in [5, 3, 8, 1, 4]:
    h.push(x)
    print("push", x, h.data)

print("pop", h.pop(), h.data)
print("pop", h.pop(), h.data)
print("pop", h.pop(), h.data)
print("pop", h.pop(), h.data)
print("pop", h.pop(), h.data)
print("pop", h.pop(), h.data)
