def normalize(input_string):
    """
    * all characters are lower case
    * white-space should be appear only once
    * no redundant space

    # More technical means
    https://towardsdatascience.com/text-normalization-for-natural-language-processing-nlp-70a314bfa646
    """
    
    # only lower chars
    res = input_string.lower()

    # on white-space
    res = res.split()
    res = " ".join(res)

    return res

print(normalize(input()))