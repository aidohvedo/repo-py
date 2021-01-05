def func_input():
    user = {'Имя':'', 'Фамилия':'', 'Год рождения':'', 'Город проживания':'','e-mail':'','Телефон':''}
    for key,value in user.items():
        value = input(f'Input {key} :')
        user[key] = value
    print(user)

func_input()

