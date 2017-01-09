def duplicate_encode(word):
    """For every non repeated word '(' for every word that is repeated in the word ')'"""
    word = list(word.lower())
    temp = word
    dupe_letters = set()
    for index, letter in enumerate(word):
        if not letter not in dupe_letters:
            for comparing_letter in temp:
                next(comparing_letter)
                if letter == comparing_letter:
                    dupe_letters.add(letter)

    print(word)

def dupe_encode(word):
    """For every non repeated word '(' for every word that is repeated in the word ')'"""
    seen = set()
    uniq = []
    word = list(word.lower())
    new_word = []
    for letter in word:
        if letter not in seen:
            seen.add(letter)
            uniq.append(letter)
    mydict = dict(zip(uniq, [0 for y in word]))
    for x in word:
        if x in uniq:
            mydict[x] += 1
    for x in word:
        if mydict[x] > 1:
            new_word.append(')')
        elif mydict[x] < 2:
            new_word.append('(')
    for x in new_word:
        print(x)
    new_string = ''.join(new_word)
    print(new_string)
    return new_string

def duplicate_encode_solution(word):
   return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

dupe_encode("Success")