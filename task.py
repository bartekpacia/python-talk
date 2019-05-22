# Znajdź liczbę mniejszą od 1000, która:
# - podzielona przez 10 daje resztę 9
# - podzielona przez 15 daje resztę 14
# - podzielona przez 21 daje resztę 20

for i in range(0, 1000):
    if i % 10 == 9:
        if i % 15 == 14:
            if i % 21 == 20:
                print(i)
