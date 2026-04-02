def bpe_tokenize_verbose(word: str, merges: list[tuple[str, str]]) -> list[str]:
    result_tokens = list(word)

    # main loop
    while True:
        merged = False

        # iterate over the merging rules
        for merging_rule in merges:
            a, b = merging_rule

            for i in range(len(result_tokens) - 1):
                if result_tokens[i] == a and result_tokens[i + 1] == b:

                    # merge and update the tokens
                    result_tokens[i] = a + b
                    result_tokens.pop(i + 1)
                    merged = True
                    break

            # only one merge per a step
            if merged:
                break

        # breaking condition
        if not merged:
            break

    return result_tokens


word = "banana"
merges = [("a", "n"), ("an", "a"), ("b", "a")]

tokens = bpe_tokenize_verbose(word, merges)
# ['b', 'a', 'n', 'a', 'n', 'a']
# ['b', 'an', 'a', 'n', 'a']
# ['b', 'an', 'an', 'a']
# ['b', 'an', 'ana']
print(tokens)
