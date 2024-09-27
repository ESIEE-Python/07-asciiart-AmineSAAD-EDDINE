"""cette fontion permet d'encoder une chaîne de caractères"""
def artcode_i(s):
    trtab = str.maketrans('àâãäçèéêëìíîïñòóôõöšùúûüýÿž', 'aaaaceeeeiiiinooooosuuuuyyz')
    s = s.translate(trtab)
    if len(s) == 0:
        return []
    liste = []
    compteur = 1
    lettre = s[0]
    for i in range(1, len(s)):
        if s[i] == lettre:
            compteur += 1
        else:
            liste.append((lettre, compteur))
            lettre = s[i]
            compteur = 1
    liste.append((lettre, compteur))
    return list

def artcode_r(s):
    trtab = str.maketrans('àâãäçèéêëìíîïñòóôõöšùúûüýÿž', 'aaaaceeeeiiiinooooosuuuuyyz')
    s = s.translate(trtab)
    if len(s) == 0:
        return []
    liste = []
    compteur = 1
    lettre = s[0]
    for i in range(1, len(s)):
        if s[i] == lettre:
            compteur += 1
        else:
            liste.append((lettre, compteur))
            lettre = s[i]
            compteur = 1
    liste.append((lettre, compteur))
    return liste

def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
