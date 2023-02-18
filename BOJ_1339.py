import sys
input = sys.stdin.readline

alphabet_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

def bruteforce(N, numbers):
    answer = 0
    using_list = []
    
    for number in numbers:
        for i in range(len(number)):
            num = 10 ** (len(number)-i - 1)
            alphabet_dict[number[i]] += num
    # print(alphabet_dict)
    for value in alphabet_dict.values():
        if value > 0: using_list.append(value)
    # print(using_list)

    sorted_list = sorted(using_list, reverse=True)
    for i in range(len(sorted_list)):
        answer += sorted_list[i] * (9 - i)

    print(answer)
    return

if __name__ == '__main__':
    N = int(input())
    numbers = [list(input())[:-1] for _ in range(N)]

    bruteforce(N, numbers)
