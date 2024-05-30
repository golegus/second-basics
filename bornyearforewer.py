while True:
    bornyear=int(input('Год рождения Пушкина А.С.:'))
    if bornyear<1799:
        print('Позже. Попробуй еще раз.')
        continue
    elif bornyear>1799:
        print('Раньше. Попробуй еще раз. ')
        continue
    else:
        print('Верно')
        break


