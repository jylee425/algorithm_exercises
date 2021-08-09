def toCamelCase(under_score_str):
    res = ""

    if under_score_str.count("_") == 0:
        res = under_score_str
    else:
        tokens = under_score_str.split("_")
        tokens = [t for t in tokens if t != ""]

        for i, t in enumerate(tokens):
            if i == 0:
                res += t.lower()
            else:
                res += t[0].upper()
                if len(t) > 1:
                    res += t[1:].lower()

    return res

print(toCamelCase(input()))