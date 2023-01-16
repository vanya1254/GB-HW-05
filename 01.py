# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'


from random import randint

def check_amount():
    condition_amount = True
    
    while condition_amount:
        amount = int(input('Введите общее число конфет => '))
        if amount >= 100:
            condition_amount = False
            return amount
        else:
            print('Можно задать число конфет только от 100')
        

def check_user_step(step):
    return 0 < step <= 28

                                                                                                # хотел эти две проверки через лямбду записать, не получилось(обернул лямбду в бул всегда тру возвращает)
def check_amount_step(amount, step):
    return amount >= step


def user_steps(user_name, amount):
    condition_step = True
    print()
    while condition_step:
        user_step = int(input(f'Ход игрока {user_name}, осталось конфет: {amount} => '))
        if check_user_step(user_step) and check_amount_step(amount, user_step):
            amount -= user_step
            condition_step = False
        else:
            print(f'Можно брать от 1 до 28 конфет за раз и не больше {amount}')
    
    return amount


def bot_steps(botname, amount):
    print()
    bot_step = int(amount % 29)
    
    if bot_step == 0:
        bot_step += randint(1, 28)
        
    print(f'Ход игрока {botname}, осталось конфет: {amount} => {bot_step}')
    amount -= bot_step
    
    return amount


def game_pvp(username_1, username_2, amount, winner = ''):
    while amount > 0:
        amount = user_steps(username_1, amount)
        if amount == 0:
            winner += username_1
            break

        amount = user_steps(username_2, amount)
        if amount == 0:
            winner += username_2
    
    return winner

                                                                                                # прям чувствую эти функции можно объединить в одну без повторения кода, но не придумал как
def game_pve(username, amount, botname = 'БОТ - ИВАН', winner = ''):
    while amount > 0:
        amount = user_steps(username, amount)
        if amount == 0:
            winner += username
            break

        amount = bot_steps(botname, amount)
        if amount == 0:
            winner += botname
    
    return winner

print('\n\nДобро пожаловать в игру с конфетами!\n\n')
print('Правила игры:\n \
    На столе лежит заданное количество конфет.\n \
    Играют два игрока делая ход друг после друга.\n \
    Первый ход определяется жеребьёвкой.\n \
    За один ход можно забрать не более чем 28 конфет.\n \
    Все конфеты оппонента достаются сделавшему последний ход.\n\n')

amount_candies = check_amount()
bot_or_not = input('Игра с другом ("д") или ботом ("б") => ')

if bot_or_not == 'д':
    user_1_name = (input('Первый игрок, как к вам обращаться? => '))
    user_2_name = (input('Второй игрок, как к вам обращаться? => '))
    name_winner = game_pvp(user_1_name, user_2_name, amount_candies)
elif bot_or_not == 'б':
    user_name = (input('Как к вам обращаться? => '))
    name_winner = game_pve(user_name, amount_candies)
    pass

print(f'\n\nПоздравляем, {name_winner}, ты забираешь все конфеты!')                             # обидно конечно если боту проигрываешь, что его поздравляют, но решил так оставить