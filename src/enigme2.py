import itertools
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def findValidMapping(word1, word2, result):
    word1_letters = list(word1)
    word2_letters = list(word2)
    result_letters = list(result)
    unique_letters = list(set(word1_letters + word2_letters + result_letters))
    word1_first_letter = word1_letters[0]
    word2_first_letter = word2_letters[0]
    mapping = {}
    for attempt in itertools.permutations(digits, len(unique_letters)):
        for index, letter in enumerate(unique_letters):
            mapping[letter] = attempt[index]

        if mapping[word1_first_letter] == 0 or mapping[word2_first_letter] == 0:
            continue

        first_number = convertWordToNumber(word1_letters, mapping)
        second_number = convertWordToNumber(word2_letters, mapping)
        result_number = convertWordToNumber(result_letters, mapping)
        if first_number + second_number == result_number:
            return mapping

def convertWordToNumber(word, mapping):
    n = 0
    letters = list(word)
    for index, letter in enumerate(letters):
        n += mapping[letter] * (10 ** (len(letters) - index - 1))
    return n

print(findValidMapping('SEND', 'MORE', 'MONEY'))
print(findValidMapping('CHEVAL', 'VACHE', 'OISEAU'))
print(findValidMapping('HUIT', 'HUIT', 'SEIZE'))