bornyears = {
    'Гвидо Ван Россум': 1956,
    'Линус Торвальдс': 1969,
    'Пол Маккартни': 1942,
    'Михаил Гельфанд': 1963,
    'Мария Кюри': 1867
}
answers = {}
answer = None
while answer is not True:
    for person in bornyears:
        answer_year = int(input(f'Год рождения {person} ?'))
        if answer_year==bornyears[person]:
            answers[person] = True
        else:
            answers[person] = False
    count_true = sum(value is True for value in answers.values())
    print(f'Вы ответили правильно на {count_true} вопросов.')
    print(f'Вы ошиблись {len(answers)-count_true} раз/а.')
    print(f'Доля правильных ответов {count_true*100/len(answers)}%.')
    print(f'Доля неправильных ответов {(len(answers)-count_true)*100/len(answers)}%.')
    answer = input('Если хотите попробовать еще раз - напечатайте "да".')
    if answer != "да":
        answer = True


