if __name__ == "__main__":
    N, M = map(int, input().split())

    pokemon_dictionary = {}
    for idx in range(N):
        name = str(input())

        pokemon_dictionary[name] = idx + 1
        pokemon_dictionary[str(idx + 1)] = name

    for _ in range(M):
        problem_key = str(input())
        print(pokemon_dictionary[problem_key])
