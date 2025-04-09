def pow(a, b, c):
    if b == 0:
        return 1

    if b % 2 == 0:
        power = pow(a, b // 2, c) ** 2
    else:
        power = pow(a, b // 2, c) ** 2 * a

    power = power % c
    return power


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    print(pow(A, B, C))
