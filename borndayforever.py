bornyear = None
bornday = None

while bornyear != 1799:
    bornyear = int(input('Год рождения Пушкина А.С.?'))
print('Верно!')
while bornday != 6.06:
    bornday = float(input('День рождения Пушкина А.С.?'))
print(f"Верно! Пушкин родился {bornday}.{bornyear}")