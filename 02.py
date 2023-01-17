# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом
'''

| {1} | {2} | {3} |
|-----|-----|-----|
| {4} | {5} | {6} |
|-----|-----|-----|
| {7} | {8} | {9} |

'''


from random import choice, randint


def print_gameboard(gameboard_list):
    print(f'\n\n    | {gameboard_list[0]} | {gameboard_list[1]} | {gameboard_list[2]} |\n\
    |---|---|---|\n\
    | {gameboard_list[3]} | {gameboard_list[4]} | {gameboard_list[5]} |\n\
    |---|---|---|\n\
    | {gameboard_list[6]} | {gameboard_list[7]} | {gameboard_list[8]} |\n\n')


def check_gameboard_list(gameboard_list):
    gameboard_win_list = [[0, 1, 2], [3, 4, 5],\
                          [6, 7, 8], [0, 3, 6],\
                          [1, 4, 7], [2, 5, 8],\
                          [0, 4, 8], [2, 4, 6]]

    for i in range(len(gameboard_win_list)):
        count = 0
        for j in range(len(gameboard_win_list[i])):
            if gameboard_list[gameboard_win_list[i][j]] == gameboard_list[gameboard_win_list[i][j + 1]] == gameboard_list[gameboard_win_list[i][j + 2]]:
                count += 3
            break
        if count == 3:
            return True
    
    return False


def user_steps(username, user_figure, gameboard_list):
    condition_step = True
    
    while condition_step:
            user_step = int(input(f'Ход игрока, {username}: {user_figure} => '))
            if 1 <= user_step <= 9 and (gameboard_list[user_step - 1] not in ['X', 'O']):
                condition_step = False
                gameboard_list[user_step - 1] = user_figure
                print_gameboard(gameboard_list)
            else:
                continue
    
    return gameboard_list


def bot_steps_easy_mode(botname, bot_figure, gameboard_list):
    condition_step = True
    
    while condition_step:
        bot_step = randint(1, 9)
        
        if 1 <= bot_step <= 9 and (gameboard_list[bot_step - 1] not in ['X', 'O']):
            print(f'Ход игрока, {botname}: {bot_figure} => {bot_step}')
            condition_step = False
            gameboard_list[bot_step - 1] = bot_figure
            print_gameboard(gameboard_list)
        else:
            continue
    
    return gameboard_list


def game_pvp(username_1, username_2, gameboard_list = [i for i in range(1, 10)], winner = ''):
    count_steps = 0
    condition = True
    list_X_O = ['X', 'O']
    user_1_figure = choice(list_X_O)
    list_X_O.remove(user_1_figure)
    user_2_figure = choice(list_X_O)
    print_gameboard(gameboard_list)
    
    while condition and count_steps < 10:
        count_steps += 1

        gameboard_list = user_steps(username_1, user_1_figure, gameboard_list)
        if check_gameboard_list(gameboard_list):
            condition = False
            winner += username_1
            break
        
        gameboard_list = user_steps(username_2, user_2_figure, gameboard_list)
        if check_gameboard_list(gameboard_list):
            condition = False
            winner += username_1
            break
    
    return winner


def game_pve(username_1, mode, botname = 'БОТ - ИВАН', gameboard_list = [i for i in range(1, 10)], winner = ''):
    count_steps = 0
    condition = True
    list_X_O = ['X', 'O']
    user_1_figure = choice(list_X_O)
    list_X_O.remove(user_1_figure)
    bot_figure = choice(list_X_O)
    print_gameboard(gameboard_list)
    
    while condition and count_steps < 10:
        count_steps += 1

        gameboard_list = user_steps(username_1, user_1_figure, gameboard_list)
        if check_gameboard_list(gameboard_list):
            condition = False
            winner += username_1
            break
        
        if mode == 'л':
            gameboard_list = bot_steps_easy_mode(botname, bot_figure, gameboard_list)
        elif mode == 'с':
            # gameboard_list = bot_steps_medium_mode(botname, bot_figure, gameboard_list)
            pass
        elif mode == 'т':
            # gameboard_list = bot_steps_hard_mode(botname, bot_figure, gameboard_list)
            pass
        
        if check_gameboard_list(gameboard_list):
            condition = False
            winner += username_1
            break
    
    return winner


print('\n\nДобро пожаловать в Крестики-нолики!\n\n')
print('Правила игры:\n \
    Кто первый соберет три в ряд или по диагонали,\n \
    тот и победил!\n\n')

bot_or_not = input('Игра с другом ("д") или ботом ("б") => ')

if bot_or_not == 'д':
    user_1_name = input('Первый игрок, как к вам обращаться? => ')
    user_2_name = input('Второй игрок, как к вам обращаться? => ')
    name_winner = game_pvp(user_1_name, user_2_name)
elif bot_or_not == 'б':
    user_name = input('Как к вам обращаться? => ')
    game_mode = input('Легкий("л"), Средний("с"), Тяжелый("т") => ')
    name_winner = game_pve(user_name, game_mode)
    
if name_winner != '':
    print(f'Поздравляем, {name_winner}, с победой!')
else:
    print(f'Ничья!')