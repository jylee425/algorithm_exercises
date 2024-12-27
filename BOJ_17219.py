if __name__ == "__main__":
    N, M = map(int, input().split())

    password_dictionary = {}
    for idx in range(N):
        url, password = map(str, input().split())

        password_dictionary[url] = password

    for _ in range(M):
        problem_key = str(input())
        print(password_dictionary[problem_key])
