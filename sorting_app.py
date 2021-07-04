def sort_numbers(liste):
    for i in range(0, len(liste) - 1):
        changed = False
        for j in range(0, len(liste) - 1 - i):
            if liste[j] > liste[j + 1]:
                n = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = n
                changed = True

        if not changed:
            break


liste = [3, 5, 4, 8, 6, 10]
sort_numbers(liste)

print(liste)
