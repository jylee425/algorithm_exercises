def main():
    print("Example 1")
    x = Value(2)
    y = Value(3)
    z = x + y
    print(z.data)
    z.backward()
    print(z.grad)
    print(y.grad)
    print(x.grad)

    print("Example 2")
    x = Value(2)
    y = Value(3)
    z = x * y
    print(z.data)
    z.backward()
    print(z.grad)
    print(y.grad)
    print(x.grad)

    print("Example 3")
    x = Value(2)
    y = Value(3)
    # z = 2 * x * y + x
    w = x * y
    z = w + x
    print(z.data)
    # x -->
    # y --> * --> w
    # x --------> + --> z
    # dz/dw = 1
    # dz/dy = dz/dw * dw/dx = x
    # dz/dx = dz/dw * dw/dx + 1 = y + 1
    z.backward()
    print(z.grad)
    print(y.grad)
    print(x.grad)

    print("Example 4")
    x = Value(2)
    y = Value(3)
    w = x * y
    z = w + w
    # dz/dw = 1 + 1 = 2
    # dz/dy = dz/dw * dw/dy = 2 * x = 4
    # dz/dx = dz/dw * dw/dx = 2 * y = 6
    z.backward()
    print(z.grad)
    print(w.grad)
    print(y.grad)
    print(x.grad)


class Value:
    def __init__(self, data, parents=None, local_grads=None):
        self.data = data
        self.grad = 0.0
        self.parents = parents if parents is not None else []
        self.local_grads = local_grads if local_grads is not None else []

    def __add__(self, other):
        res = Value(
            data=self.data + other.data, parents=[self, other], local_grads=[1, 1]
        )
        return res

    def __mul__(self, other):
        res = Value(
            data=self.data * other.data,
            parents=[self, other],
            local_grads=[other.data, self.data],
        )
        return res

    def backward(self):
        # build computational graph
        graph = []
        visited = set()

        def build_graph(n):
            if n not in visited:
                visited.add(n)
                for p in n.parents:
                    build_graph(p)
                graph.append(n)

        build_graph(self)

        # initialize self.grad
        self.grad = 1.0

        # back-propagate
        for n in reversed(graph):
            for p, lg in zip(n.parents, n.local_grads):
                p.grad += n.grad * lg


main()
