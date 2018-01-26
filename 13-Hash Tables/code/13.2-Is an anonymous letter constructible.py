def isLetterConstructibleFromMagazion(letterText, magazineText):
    counter = {}
    for c in letterText:
        counter[c] = counter.get(c, 0) + 1
    for c in magazineText:
        if c in counter.keys():
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]
                if len(counter) == 0:
                    break
    return len(counter) == 0


print isLetterConstructibleFromMagazion('abbcd', 'abbcde')
