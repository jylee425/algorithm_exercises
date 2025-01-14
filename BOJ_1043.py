if __name__ == "__main__":
    N, M = map(int, input().split())

    # first truth members
    truth = list(map(int, input().split()))
    truth_num, truth_list = truth[0], truth[1:]
    assert truth_num == len(truth_list)

    truth_set = set()
    for member in truth_list:
        truth_set.add(member)

    # party information
    party_list = []

    for _ in range(M):
        party = list(map(int, input().split()))
        participant_num, participants = party[0], party[1:]
        assert participant_num == len(participants)

        party_list.append(participants)

    # propagation
    for party in party_list:
        party_has_truth_member = False
        for member in party:
            if member in truth_set:
                party_has_truth_member = True
            break

        if party_has_truth_member:
            for member in party:
                if member not in truth_set:
                    truth_set.add(member)

    while True:
        propagation = False

        for party in party_list:
            is_true_group = False
            for member in party:
                if member in truth_set:
                    is_true_group = True
                    break

            if is_true_group:
                for member in party:
                    if member not in truth_set:
                        truth_set.add(member)
                        propagation = True

        if not propagation:
            break

    # check
    participatable_num = 0
    for party in party_list:
        is_true_group = False

        for member in party:
            if member in truth_set:
                is_true_group = True
            break

        if not is_true_group:
            participatable_num += 1
    print(participatable_num)
