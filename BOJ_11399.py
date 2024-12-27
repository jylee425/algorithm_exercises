if __name__ == "__main__":
    _ = int(input())
    time_consumptions = map(int, input().split())

    result = 0
    time_consumptions = sorted(time_consumptions, reverse=True)
    for idx, time_consumption in enumerate(time_consumptions):
        result += (idx + 1) * time_consumption

    print(result)
