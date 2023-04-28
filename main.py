# -*- coding: utf-8 -*-
from rich.console import Console
from modules.text import *
import modules.entity as entity
from modules.location import Location
import modules.tools as tools
import time
import modules.items as items
from modules.settings import *
import modules.saves_m as saves_m

# Init console object
console = Console()

# Init global variables
LOGO = """
\x1b[37;1m███████████████████████████████████████████████████████████████████████\x1b[;0m
\x1b[37;1m█\x1b[;0m \x1B[34;1m┏━━━━━━━━━━━┓\x1b[;0m          \x1b[37;0m┃\x1b[;0m  \x1B[31;1m┏━━━━━━━━━━━┓ \x1b[;0m \x1B[35;1m┏━━━━━━━━━━┓\x1b[;0m \x1B[35;1m┏━━━━━━━━━━━┓\x1b[;0m \x1b[37;1m█\x1b[;0m
\x1b[37;1m█\x1b[;0m \x1B[34;1m┃  ┏━━━━━━━━┛\x1b[;0m          \x1b[37;0m┃\x1b[;0m  \x1B[31;1m┃   ┏━━━━┓  ┃ \x1b[;0m \x1B[35;1m┃   ┏━━━━┓ ┃\x1b[;0m \x1B[35;1m┃  ┏━━━━━━━━┛\x1b[;0m \x1b[37;1m█\x1b[;0m
\x1b[37;1m█\x1b[;0m \x1B[34;1m┃  ┗━━━━━━━━┓\x1b[;0m  ┏━━━━┓  \x1b[37;0m┃\x1b[;0m  \x1B[31;1m┃   ┗━━━━┛  ┃ \x1b[;0m \x1B[35;1m┃   ┗━━━━┛ ┃\x1b[;0m \x1B[35;1m┃  ┃         \x1b[;0m \x1b[37;1m█\x1b[;0m
\x1b[37;1m█\x1b[;0m \x1B[34;1m┗━━━━━━━━━┓ ┃\x1b[;0m  ┃ ██ ┃  \x1b[37;0m┃\x1b[;0m  \x1B[31;1m┃   ━━━━━━┳━┛ \x1b[;0m \x1B[35;1m┃  ┏━━━━━━━┛\x1b[;0m \x1B[35;1m┃  ┃  ┏━━━━━┓\x1b[;0m \x1b[37;1m█\x1b[;0m
\x1b[37;1m█\x1b[;0m \x1B[34;1m┏━━━━━━━━━┛ ┃\x1b[;0m  ┗━━━━┛  \x1b[37;0m┃\x1b[;0m  \x1B[31;1m┃   ┏━━━┓ ┗━━┓\x1b[;0m \x1B[35;1m┃  ┃        \x1b[;0m \x1B[35;1m┃  ┃  ┗━━━┓ ┃\x1b[;0m \x1b[37;1m█\x1b[;0m
\x1b[37;1m█\x1b[;0m \x1B[34;1m┗━━━━━━━━━━━┛\x1b[;0m          \x1b[37;0m┃\x1b[;0m  \x1B[31;1m┃   ┃   ┗━┓  ┃\x1b[;0m \x1B[35;1m┃  ┃        \x1b[;0m \x1B[35;1m┃  ┗━━━━━━┛ ┃\x1b[;0m \x1b[37;1m█\x1b[;0m
\x1b[37;1m█\x1b[;0m ━━━━━━━━━━━━━          ┃  \x1B[31;1m┗━━━┛     ┗━━┛\x1b[;0m \x1B[35;1m┗━━┛         \x1b[;0m\x1B[35;1m┗━━━━━━━━━━━┛\x1b[;0m \x1b[37;1m█\x1b[;0m
\x1b[37;1m███████████████████████████████████████████████████████████████████████\x1b[;0m"""
# Commands 
NEW      = 'new'
LOAD     = 'load'
LAST     = 'last'
LIST     = 'list'
CREDITS  = 'credits'
DELETE   = 'delete'
SETTINGS = 'settings'
EXIT     = 'exit'
INV      = 'inv'
THINK    = 'think'
GO       = 'go'
TIME     = 'time'
STATUS   = 'status'
SAVE     = 'save'
TALK     = 'talk'
TAKE     = 'take'
PUT      = 'put'
LOOK     = 'look'
CRAFT    = 'craft'
# Settings commands
SET      = 'set'
DEF      = 'def'
DEFALL   = 'defall'
text_delay = float(settings['delay'][1])
class ExitException(Exception): pass # Class for exit error
class ExitFromSaveException(Exception): pass # Class for exit error
class Game:
    def l_in_commands(self, choice):
        return choice.lower().rstrip() in self.main_menu_context.keys()
    
    def l_no_params(self, choice):
        return len(choice.split(' ')) == 1
    
    def l_params(self, choice):
        return len(choice.split(' ')) == 2
    def initialition_save(self):
        # Init main menu
        self.main_menu_context = {
            NEW:('Новое сохранение',self.new),
            LOAD:('Загрузить сохранение',self.load),
            LAST:('Последние сохранение',self.last),
            LIST:('Список сохранений', self._list),
            CREDITS:('Благодарности', self.credits),
            DELETE:('Удалить сохранение', self.delete),
            SETTINGS:('Настройки',self.settings),
            EXIT:('Выход на рабочий стол',self.exit)
        }
        self.settings_menu_context = {
            SET:('Изменить значение настройки (set <название> <значение>)',),
            DEF:('Изменить значение настройки по умолчанию (def <название>)',),
            DEFALL:('Сбросить всё по умолчанию (defall)',),
            EXIT:('Выход в главное меню (exit)',)
        }
        print(LOGO) # Print a logo
        add(LOGO) # Add to untimed
        print(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m') # Print an emtpy line
        add(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m')
        self.agreetisment() # Show title welcome
        print(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m') # Print an emtpy line
        add(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m')
        self.menu() # Show all menu
        special_print('Введите название команды', color='\x1B[31;1m', _add=True)
        while True:
            print('\x1B[37;1m█\x1B[0m \x1B[35;1m-~>\x1B[;0m \x1B[31;1m', end='')
            choice = input()
            # If choice in commands
            if self.l_in_commands(choice.split(' ')[0]):
                # If in command no parameters
                if self.l_no_params(choice):
                    debug(f'Invoked: {choice.lower().rstrip()}')
                    s = self.main_menu_context[choice.lower().rstrip()][1]() # Invoke command
                    if choice.lower().rstrip() == NEW:
                        return s
                    if choice.lower().rstrip() == LOAD:
                        redrow()
                        return s
                elif self.l_params(choice) and len(choice.split(' ')) == 2:
                    if choice.split(' ')[0] == DELETE:
                        self.delete(choice.split(' ')[1])
                else:
                    special_print('Ошибка! Эта функция вызывается без параметров!', color='\x1B[31;1m', delay=0.01)
                    time.sleep(len('Ошибка! Эта функция вызывается без параметров!')/50)
                    redrow()
            else:
                special_print('Неизвестная команда!', '\x1B[31;1m')
                time.sleep(len('Неизвестная команда!')/50)
                redrow()


    # Commands functions
    def new(self):
        special_print('Введите название сохранения', '\x1B[31;1m')
        print('\x1B[37;1m█\x1B[0m \x1B[35;1m-~>\x1B[;0m \x1B[31;1m', end='')
        self.save_name = input()
        
        self.player = entity.Player(
            name='player',
            hp=10,
            items=[],
            description='Разборщик, пайщик, разбирается в электронике',
            interesting='?'
        )
        self.save = Save(self.player, self)
        saves_m.save_game(self.save_name, self.save)
        return self.save
    
    def credits(self):
        redrow()
        special_print('Над игрой работали', '\x1B[34;1m')
        # Promrammers
        special_print('Программисты', '\x1B[35;1m')
        for tester in open('credits/programmers.txt', 'r').readlines():
            print(f'\x1B[37;1m█\x1B[0m \x1B[34;1m@\x1b[;1m', end='')
            delay_print(tester.rstrip(), '\x1B[35;3m', end='')
            print(' '*(INSIDE_TEXT_SIZE-len('@'+tester.rstrip())-1)+'\x1B[37;1m█\x1B[0m')
        # Desingers
        special_print('Дизайнеры', '\x1B[35;1m')
        for tester in open('credits/desingers.txt', 'r').readlines():
            print(f'\x1B[37;1m█\x1B[0m \x1B[34;1m@\x1b[;1m', end='')
            delay_print(tester.rstrip(), '\x1B[35;3m', end='')
            print(' '*(INSIDE_TEXT_SIZE-len('@'+tester.rstrip())-1)+'\x1B[37;1m█\x1B[0m')
        # Testers
        special_print('Тестеры', '\x1B[35;1m')
        for tester in open('credits/testers.txt', 'r').readlines():
            print(f'\x1B[37;1m█\x1B[0m \x1B[34;1m@\x1b[;1m', end='')
            delay_print(tester.rstrip(), '\x1B[35;2m', end='')
            print(' '*(INSIDE_TEXT_SIZE-len('@'+tester.rstrip())-1)+'\x1B[37;1m█\x1B[0m')
        # Servers
        special_print('Спасибо дискорд серверам за продвижение проекта', '\x1B[35;1m')
        for tester in open('credits/ds_servers.txt', 'r').readlines():
            special_print(tester, '\x1B[34;1m')
        special_print('EternalArts Team 2023. All rights reserved.', '\x1B[37;1m')
    
    def delete(self, arg):
        if arg in saves_m.saves():
            redrow()
            saves_m.delete(arg)
            special_print(f'Удалено: {arg}', '\x1B[31;1m')
        else:
            special_print(f'Не удаётся найти указанное сохранение {arg}', '\x1B[31;1m')
            time.sleep(len(f'Не удаётся найти указанное сохранение {arg}')/50)
            redrow()

    def load(self):
        redrow()
        special_print('Введите название сохранения', '\x1B[31;1m', _add=True)
        while True:
            print('\x1B[37;1m█\x1B[0m \x1B[35;1m-~>\x1B[;0m \x1B[31;1m', end='')
            self.save_name = input()
            if self.save_name in saves_m.saves():
                break
        self.save = saves_m.load_game(self.save_name)
        return self.save

    def last(self):
        print('last')
    def _list(self):
        redrow()
        special_print('Ваши сохранения', '\x1B[34;1m')
        for save_name in saves_m.saves():
            special_print(save_name, '\x1B[34;1m')
    def settings(self):
        global settings
        del untimed_text[2:-1]
        redrow()
        self.settings_menu_commands()
        special_print('Настройки', '\x1B[34;1m')
        self.settings_menu()
        while True:
            print('\x1B[37;1m█\x1B[0m \x1B[35;1m-~>\x1B[;0m \x1B[31;1m', end='')
            choice = input()
            # If choice in commands
            if choice.lower().split(' ')[0] in self.settings_menu_context.keys():
                if choice.lower().split(' ')[0] == SET:
                    if len(choice.lower().split(' ')) == 3:
                        option_name = choice.lower().split(' ')[1]
                        arg = choice.lower().split(' ')[2]
                        if option_name in settings.keys():
                            if settings_cheacking_funcs[option_name](arg): # Invoke cheack function
                                settings[option_name][1] = arg
                                update_settings()
                                special_print('Изменено', color='\x1B[33;1m')
                                time.sleep(len('Изменено')/50)
                                redrow()
                                special_print('Настройки', '\x1B[37;1m')
                                self.settings_menu2()
                            else:
                                special_print('Ошибка! Неверный параметр', color='\x1B[31;1m', delay=0.01)
                                time.sleep(len('Ошибка! Неверный параметр')/50)
                                redrow()
                                special_print('Настройки', '\x1B[37;1m')
                                self.settings_menu2()
                        else:
                            special_print('Ошибка! Неизвестная настройка', color='\x1B[31;1m', delay=0.01)
                            time.sleep(len('Ошибка! Неизвестная настройка')/50)
                            redrow()
                            self.settings_menu2()
                elif choice.lower().rstrip() == EXIT:
                    del untimed_text[1:7]
                    redrow()
                    print(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m') # Print an emtpy line
                    add(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m')
                    self.agreetisment() # Show title welcome
                    print(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m') # Print an emtpy line
                    add(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m')
                    self.menu() # Show all menu
                    special_print('Введите название команды', color='\x1B[31;1m', _add=True)
                    break
                    
                elif choice.lower().split(' ')[0] == DEF:
                    if len(choice.lower().split(' ')) == 2:
                        option_name = choice.lower().split(' ')[1]
                        if option_name in settings.keys():
                            settings[option_name] = default_settings[option_name]
                            update_settings()
                            special_print('Изменено', color='\x1B[35;1m')
                            time.sleep(len('Изменено')/50)
                            redrow()
                        else:
                            special_print('Ошибка! Неизвестная настройка', color='\x1B[31;1m', delay=0.01)
                            time.sleep(len('Ошибка! Неизвестная настройка')/50)
                            redrow()
                            special_print('Настройки', '\x1B[37;1m')
                            self.settings_menu2()

                elif choice.lower().rstrip() == DEFALL:
                    settings = default_settings
                    update_settings()
                    special_print('Изменено по умолчанию', '\x1B[35;1m')
                    time.sleep(len('Изменено по умолчанию')/30)
                    redrow()
                    special_print('Настройки', '\x1B[37;1m')
                    self.settings_menu2()
            else:
                special_print('Неизвестная команда!', '\x1B[31;1m')
                time.sleep(len('Неизвестная команда!')/30)
                redrow()
                special_print('Настройки', '\x1B[34;1m')
                self.settings_menu2()

    def settings_menu_commands(self):
        for (name, values) in self.settings_menu_context.items():
            print(f'\x1B[37;1m█\x1B[0m ', end='')
            time.sleep(0.25)
            print(f'\x1B[34;1m{name}\x1B[;0m', end='')
            print('\x1B[37;1m - \x1b[;0m', end='')
            delay_print(f'{values[0]}', '\x1B[35;1m', end='')
            print(' '*(INSIDE_TEXT_SIZE-len(name+' - '+values[0])-2)+' \x1B[37;1m█\x1B[0m')
            add('\x1B[37;1m█\x1B[0m '+'\x1B[34;1m'+name+'\x1B[37;1m - \x1b[;0m'+'\x1B[;0m'+'\x1B[35;1m'+values[0]+'\x1B[;0m'+' '*(INSIDE_TEXT_SIZE-len(name+' - '+values[0])-2)+' \x1B[37;1m█\x1B[0m')

    def settings_menu(self):
        for (name, values) in settings.items():
            print(f'\x1B[37;1m█\x1B[0m ', end='')
            time.sleep(0.20)
            print(f'\x1B[34;1m{name}\x1B[;0m', end='')
            print('\x1B[37;1m - \x1b[;0m', end='')
            delay_print(f'{values[0]}', '\x1B[35;1m', end='')
            print('\x1B[37;1m - \x1b[;0m', end='')
            if values[1] == 'false':
                delay_print(f'{values[1]}', '\x1B[31;1m', end='')
            elif values[1] == 'true':
                delay_print(f'{values[1]}', '\x1B[33;1m', end='')
            else:
                delay_print(f'{values[1]}', '\x1B[37;1m', end='')
            print(' '*(INSIDE_TEXT_SIZE-len(name+' - '+str(values[0])+' - '+str(values[1]))-2)+' \x1B[37;1m█\x1B[0m')

    def settings_menu2(self):
        for (name, values) in settings.items():
            print(f'\x1B[37;1m█\x1B[0m ', end='')
            time.sleep(0.25)
            print(f'\x1B[34;1m{name}\x1B[;0m', end='')
            print('\x1B[37;1m - \x1b[;0m', end='')
            print(f'\x1B[35;1m{values[0]}\x1B[;0m', end='')
            print('\x1B[37;1m - \x1b[;0m', end='')
            if values[1] == 'false':
                delay_print(f'{values[1]}', '\x1B[31;1m', end='')
            elif values[1] == 'true':
                delay_print(f'{values[1]}', '\x1B[33;1m', end='')
            else:
                delay_print(f'{values[1]}', '\x1B[37;1m', end='')
            print(' '*(INSIDE_TEXT_SIZE-len(name+' - '+str(values[0])+' - '+str(values[1]))-2)+' \x1B[37;1m█\x1B[0m')

    def exit(self):
        special_print('Вы действительно хотите выйти?y/n', '\x1B[31;1m')
        while True:
            print('\x1B[37;1m█\x1B[0m \x1B[35;1m-~>\x1B[;0m \x1B[31;1m', end='')
            choice = input()
            if choice.lower().rstrip() == 'y':
                raise ExitException
            elif choice.lower().rstrip() == 'n':
                redrow()

    def agreetisment(self):
        print('\x1B[37;1m█\x1B[0m ', end='')
        delay_print('Добро пожаловать в ', '\x1B[34;1m', end='', delay=text_delay)
        delay_print('S', '\x1B[34;1m', end='', delay=text_delay)
        delay_print('R', '\x1B[31;1m', end='', delay=text_delay)
        delay_print('PG', '\x1B[35;1m', end='', delay=text_delay)
        delay_print('!', '\x1B[36;5m', end='', delay=text_delay)
        print(' '*(INSIDE_TEXT_SIZE-len("Добро пожаловать в SRPG!")-1)+'\x1B[37;1m█\x1B[0m')
        add('\x1B[37;1m█\x1B[0m '+'\x1B[34;1mДобро пожаловать в S\x1B[31;1mR\x1B[;0m\x1B[35;1mPG\x1B[;0m\x1B[34;5m!\x1B[;0m'+' '*(INSIDE_TEXT_SIZE-len("Добро пожаловать в SRPG!")-1)+'\x1B[37;1m█\x1B[0m')
    
    def menu(self):
        for (number, context) in self.main_menu_context.items():
            print(f'\x1B[37;1m█\x1B[0m \x1B[34;1m{number}\x1b[;0m', end='')
            print('\x1B[37;1m - \x1b[;0m', end='')
            time.sleep(0.20)
            delay_print(context[0], '\x1B[35;1m', end='', delay=text_delay)
            print(' '*(INSIDE_TEXT_SIZE-len(number+' - '+context[0])-1)+'\x1B[37;1m█\x1B[0m')
            add(f'\x1B[37;1m█\x1B[0m \x1B[34;1m{number}\x1B[37;1m - \x1b[;0m\x1b[;0m\x1B[35;1m{context[0]}\x1B[0m'+' '*(INSIDE_TEXT_SIZE-len(f'{number} - {context[0]}')-2)+' \x1B[37;1m█\x1B[0m') # Context[0] is command description

# Данные которые нужно сохранять
# Объект игрока
# Локации
# Команды игры
# new
# load
# list
# last
# delete
# settings
# exit

# Команды игрока
# inv - инвентарь
# think - посмотреть, что думает герой
# go - перейти в другую локацию
# talk - поговорить
# take - взять предмет
# pute - положить предмет
# craft - скрафтить что-то
# use - использовать
# look - осмотреться
# exit - выход в главное меню

class Save:
    def __init__(self, player: entity.Player, game: Game) -> None:
        self.initialition_locations()
        # Init attributes
        self.player: entity.Player = player
        self.player.total_location: Location = self.location
        self.game: Game = game
        # Init menu
        self.params_commands = [GO, TALK, TAKE, PUT, CRAFT]
        self.no_params_commands = [INV, THINK, LOOK, SAVE, EXIT, SETTINGS]
        self.menu_context = {
            INV:('Инвентарь',self.inv),
            THINK:('Посмотреть, что думает герой',self.think),
            GO:('Передвижение (go <номер>)',self.go),
            LOOK:('Осмотреться', self.look),
            TALK:('Поговорить',self.talk),
            TAKE:('Взять предмет',self.take),
            SAVE:('Сохранить игру', self._save),
            PUT:('Положить предмет',self.put),
            SETTINGS:('Настройки',self.settings),
            CRAFT:('Скрафтить что-то',self.craft),
            EXIT:('Выйти в главное меню',self.exit),
        }
        self.settings_menu_context = {
            SET:('Изменить значение настройки (set <название> <значение>)',),
            DEF:('Изменить значение настройки по умолчанию (def <название>)',),
            DEFALL:('Сбросить всё по умолчанию (defall)',),
            EXIT:('Выход в главное меню (exit)',)
        }
        
    def l_in_commands(self, choice):
        return choice.lower().rstrip() in self.menu_context.keys()
    
    def l_no_params(self, choice):
        return len(choice.split(' ')) == 1
    
    def l_params(self, choice):
        return len(choice.split(' ')) == 2
    
    def main(self):
        del untimed_text[2:-1]
        redrow()
        # Show menu
        self.menu()
        special_print('Введите название команды', color='\x1B[31;1m', _add=True)
        while True:
            print('\x1B[37;1m█\x1B[0m \x1B[35;1m-~>\x1B[;0m \x1B[31;1m', end='')
            choice = input()
            print('\x1B[;0m')
            # If choice in commands
            if self.l_in_commands(choice.split(' ')[0]):
                # If in command no parameters
                if self.l_no_params(choice) and choice.lower().rstrip() in self.no_params_commands:
                    if choice.lower().rstrip() == INV:
                        self.inv()
                    elif choice.lower().rstrip() == THINK:
                        self.think()
                    elif choice.lower().rstrip() == LOOK:
                        self.look()
                    elif choice.lower().rstrip() == SAVE:
                        self._save()
                    elif choice.lower().rstrip() == SETTINGS:
                        self.settings()
                    elif choice.lower().rstrip() == EXIT:
                        self.exit()
                    debug(f'Invoked: {choice.lower().rstrip()}')
                # If in command parameters
                if self.l_params(choice) and choice.split(' ')[0] in self.params_commands:
                    if choice.split(' ')[0] == TALK and len(choice.split(' ')) == 2:
                        if choice.split(' ')[1] in self.player.total_location.entities.keys():
                            self.talk(choice.split(' ')[1])
                            debug(f'Invoked: {choice.lower().rstrip()}')
                        else:
                            special_print('Неверный номер', '\x1B[31;1m')
                            time.sleep(len('Неверный номер')/50)
                            redrow()
                    elif choice.split(' ')[0] == TAKE and len(choice.split(' ')) == 2:
                        if choice.split(' ')[1] in self.player.total_location.items.keys():
                            self.take(choice.split(' ')[1])
                            debug(f'Invoked: {choice.lower().rstrip()}')
                        else:
                            special_print('Неверный номер', '\x1B[31;1m')
                            time.sleep(len('Неверный номер')/50)
                            redrow()
                    elif choice.split(' ')[0] == GO and len(choice.split(' ')) == 2:
                        if choice.split(' ')[1] in self.player.total_location.under_locs.keys() or choice.split(' ')[1].lower() == 'e':
                            self.go(choice.split(' ')[1])
                            debug(f'Invoked: {choice.lower().rstrip()}')
                        else:
                            special_print('Неверный номер', '\x1B[31;1m')
                            time.sleep(len('Неверный номер')/50)
                            redrow()

                elif self.l_no_params(choice) and choice.split(' ')[0].lower().rstrip() in self.params_commands:
                    special_print('Ошибка! Эта функция вызывается с параметрами!', color='\x1B[31;1m', delay=0.01)
                    time.sleep(len('Ошибка! Эта функция вызывается с параметрами!')/50)
                    redrow()
                elif self.l_params(choice) and choice.split(' ')[0].lower().rstrip() in self.no_params_commands:
                    special_print('Ошибка! Эта функция вызывается без параметров!', color='\x1B[31;1m', delay=0.01)
                    time.sleep(len('Ошибка! Эта функция вызывается без параметров!')/50)
                    redrow()
            else:
                special_print('Неизвестная команда!', '\x1B[31;1m')
                time.sleep(len('Неизвестная команда!')/50)
                redrow()

    def inv(self):
        redrow()
        special_print('Ваши вещи:', '\x1B[35;1m')
        if self.player.items != {}:
            for (num, item) in self.player.items.items():
                print(f'\x1B[37;1m█\x1B[0m \x1B[34;1m{num}\x1B[37;1m - \x1B[;1m\x1B[34;1m{item.name}. \x1b[;1m', end='')
                time.sleep(0.2)
                delay_print(item.description, '\x1B[35;1m', end='', delay=text_delay)
                print(' '*(INSIDE_TEXT_SIZE-len(f'{num}.{item.name}'+' - '+item.description)-1)+'\x1B[37;1m█\x1B[0m')
        else:
            special_print('(ничего)', '\x1B[30;1m')

    def think(self):
        redrow()
        special_print(self.player.total_think, '\x1B[36;1m')
    def go(self, arg):
        redrow()
        if arg.lower() == 'e':
            if self.player.total_location.parent != None:
                self.player.total_location: Location = self.player.total_location.parent
        else:
            self.player.total_location: Location = self.player.total_location.under_locs[arg]
        self.look()

    def _save(self):
        redrow()
        saves_m.save_game(self.game.save_name, self)
        special_print('Сохранено', '\x1B[34;1m')

    def look(self):
        redrow()
        special_print(f'Вы находитесь в {self.player.total_location.name}', '\x1B[35;1m')
        if self.player.total_location.under_locs != {}:
            special_print('Локации', '\x1B[35;1m')
            for (num, loc) in self.player.total_location.under_locs.items():
                print(f'\x1B[37;1m█\x1B[0m \x1B[36;1m{num} - \x1b[;1m', end='')
                delay_print(f'{loc.name}. {loc.description}. {loc.interesting}', '\x1B[35;1m', end='')
                print(' '*(INSIDE_TEXT_SIZE-len(f"{num} - {loc.name}. {loc.description}. {loc.interesting}")-1)+'\x1B[37;1m█\x1B[0m')
        if self.player.total_location.items != {}:
            special_print('Предметы', '\x1B[35;1m')
            for (num, item) in self.player.total_location.items.items():
                print(f'\x1B[37;1m█\x1B[0m \x1B[36;1m{num} - \x1b[;1m', end='')
                delay_print(f'{item.name}. {item.description}. {item.interesting}', '\x1B[35;1m', end='')
                print(' '*(INSIDE_TEXT_SIZE-len(f"{num} - {item.name}. {item.description}. {item.interesting}")-1)+'\x1B[37;1m█\x1B[0m')
        if self.player.total_location.entities != {}:
            special_print('Персонажи', '\x1B[35;1m')
            for (num, ent) in self.player.total_location.entities.items():
                print(f'\x1B[37;1m█\x1B[0m \x1B[36;1m{num} - \x1b[;1m', end='')
                delay_print(f'{ent.name}. {ent.description}. {ent.interesting}', '\x1B[35;1m', end='')
                print(' '*(INSIDE_TEXT_SIZE-len(f"{num} - {ent.name}. {ent.description}. {ent.interesting}")-1)+'\x1B[37;1m█\x1B[0m')
        if self.player.total_location.parent != None:
            print(f'\x1B[37;1m█\x1B[0m \x1B[31;1me - \x1b[;1m', end='')
            delay_print(f'{self.player.total_location.parent.name}. {self.player.total_location.parent.description}. {self.player.total_location.parent.interesting}', '\x1B[35;1m', end='')
            print(' '*(INSIDE_TEXT_SIZE-len(f"e - {self.player.total_location.parent.name}. {self.player.total_location.parent.description}. {self.player.total_location.parent.interesting}")-1)+'\x1B[37;1m█\x1B[0m')

    def talk(self, arg: str):
        redrow()
        self.player.total_location.entities[arg].start_dialog()

    def take(self, arg: str):
        self.player.items[str(len(self.player.items)+1)] = self.player.total_location.items[arg]
        special_print(f'Вы подобрали: {self.player.total_location.items[arg].name}', '\x1B[35;1m')
        self.player.total_location.del_item(arg)
        
    def put(self): print('put')
    def craft(self): print('craft')
    def exit(self):
        special_print('Вы действительно хотите выйти?y/n', '\x1B[31;1m')
        while True:
            print('\x1B[37;1m█\x1B[0m \x1B[35;1m-~>\x1B[;0m \x1B[31;1m', end='')
            choice = input()
            if choice.lower().rstrip() == 'y':
                raise ExitFromSaveException
            elif choice.lower().rstrip() == 'n':
                redrow()

    def settings(self):
        global settings
        del untimed_text[2:-1]
        redrow()
        self.settings_menu_commands()
        special_print('Настройки', '\x1B[34;1m')
        self.settings_menu()
        while True:
            print('\x1B[37;1m█\x1B[0m \x1B[35;1m-~>\x1B[;0m \x1B[31;1m', end='')
            choice = input()
            # If choice in commands
            if choice.lower().split(' ')[0] in self.settings_menu_context.keys():
                if choice.lower().split(' ')[0] == SET:
                    if len(choice.lower().split(' ')) == 3:
                        option_name = choice.lower().split(' ')[1]
                        arg = choice.lower().split(' ')[2]
                        if option_name in settings.keys():
                            if settings_cheacking_funcs[option_name](arg): # Invoke cheack function
                                settings[option_name][1] = arg
                                update_settings()
                                special_print('Изменено', color='\x1B[33;1m')
                                time.sleep(len('Изменено')/50)
                                redrow()
                                special_print('Настройки', '\x1B[37;1m')
                                self.settings_menu2()
                            else:
                                special_print('Ошибка! Неверный параметр', color='\x1B[31;1m', delay=0.01)
                                time.sleep(len('Ошибка! Неверный параметр')/50)
                                redrow()
                                special_print('Настройки', '\x1B[37;1m')
                                self.settings_menu2()
                        else:
                            special_print('Ошибка! Неизвестная настройка', color='\x1B[31;1m', delay=0.01)
                            time.sleep(len('Ошибка! Неизвестная настройка')/50)
                            redrow()
                            self.settings_menu2()
                elif choice.lower().rstrip() == EXIT:
                    del untimed_text[1:7]
                    redrow()
                    print(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m') # Print an emtpy line
                    add(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m')
                    self.agreetisment() # Show title welcome
                    print(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m') # Print an emtpy line
                    add(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m')
                    self.menu() # Show all menu
                    special_print('Введите название команды', color='\x1B[31;1m', _add=True)
                    break
                    
                elif choice.lower().split(' ')[0] == DEF:
                    if len(choice.lower().split(' ')) == 2:
                        option_name = choice.lower().split(' ')[1]
                        if option_name in settings.keys():
                            settings[option_name] = default_settings[option_name]
                            update_settings()
                            special_print('Изменено', color='\x1B[35;1m')
                            time.sleep(len('Изменено')/50)
                            redrow()
                        else:
                            special_print('Ошибка! Неизвестная настройка', color='\x1B[31;1m', delay=0.01)
                            time.sleep(len('Ошибка! Неизвестная настройка')/50)
                            redrow()
                            special_print('Настройки', '\x1B[37;1m')
                            self.settings_menu2()

                elif choice.lower().rstrip() == DEFALL:
                    settings = default_settings
                    update_settings()
                    special_print('Изменено по умолчанию', '\x1B[35;1m')
                    time.sleep(len('Изменено по умолчанию')/30)
                    redrow()
                    special_print('Настройки', '\x1B[37;1m')
                    self.settings_menu2()
            else:
                special_print('Неизвестная команда!', '\x1B[31;1m')
                time.sleep(len('Неизвестная команда!')/30)
                redrow()
                special_print('Настройки', '\x1B[34;1m')
                self.settings_menu2()

    def settings_menu_commands(self):
        for (name, values) in self.settings_menu_context.items():
            print(f'\x1B[37;1m█\x1B[0m ', end='')
            time.sleep(0.25)
            print(f'\x1B[34;1m{name}\x1B[;0m', end='')
            print('\x1B[37;1m - \x1b[;0m', end='')
            delay_print(f'{values[0]}', '\x1B[35;1m', end='')
            print(' '*(INSIDE_TEXT_SIZE-len(name+' - '+values[0])-2)+' \x1B[37;1m█\x1B[0m')
            add('\x1B[37;1m█\x1B[0m '+'\x1B[34;1m'+name+'\x1B[37;1m - \x1b[;0m'+'\x1B[;0m'+'\x1B[35;1m'+values[0]+'\x1B[;0m'+' '*(INSIDE_TEXT_SIZE-len(name+' - '+values[0])-2)+' \x1B[37;1m█\x1B[0m')

    def settings_menu(self):
        for (name, values) in settings.items():
            print(f'\x1B[37;1m█\x1B[0m ', end='')
            time.sleep(0.20)
            print(f'\x1B[34;1m{name}\x1B[;0m', end='')
            print('\x1B[37;1m - \x1b[;0m', end='')
            delay_print(f'{values[0]}', '\x1B[35;1m', end='')
            print('\x1B[37;1m - \x1b[;0m', end='')
            if values[1] == 'false':
                delay_print(f'{values[1]}', '\x1B[31;1m', end='')
            elif values[1] == 'true':
                delay_print(f'{values[1]}', '\x1B[33;1m', end='')
            else:
                delay_print(f'{values[1]}', '\x1B[37;1m', end='')
            print(' '*(INSIDE_TEXT_SIZE-len(name+' - '+str(values[0])+' - '+str(values[1]))-2)+' \x1B[37;1m█\x1B[0m')

    def settings_menu2(self):
        for (name, values) in settings.items():
            print(f'\x1B[37;1m█\x1B[0m ', end='')
            time.sleep(0.25)
            print(f'\x1B[34;1m{name}\x1B[;0m', end='')
            print('\x1B[37;1m - \x1b[;0m', end='')
            print(f'\x1B[35;1m{values[0]}\x1B[;0m', end='')
            print('\x1B[37;1m - \x1b[;0m', end='')
            if values[1] == 'false':
                delay_print(f'{values[1]}', '\x1B[31;1m', end='')
            elif values[1] == 'true':
                delay_print(f'{values[1]}', '\x1B[33;1m', end='')
            else:
                delay_print(f'{values[1]}', '\x1B[37;1m', end='')
            print(' '*(INSIDE_TEXT_SIZE-len(name+' - '+str(values[0])+' - '+str(values[1]))-2)+' \x1B[37;1m█\x1B[0m')

    def initialition_locations(self):
        self.location = Location('Room1', 'Just a room', entities=[entity.test_ent], items=[items.test_item,items.test_item]).add([
            Location('Room2 in room 1', 'Just a room')]
        )
    
    def menu(self):
        for (name, context) in self.menu_context.items():
            print(f'\x1B[37;1m█\x1B[0m \x1B[34;1m{name}\x1b[;1m', end='')
            print('\x1B[37;1m - \x1B[;0m', end='')
            time.sleep(0.20)
            delay_print(context[0], '\x1B[35;1m', end='')
            print(' '*(INSIDE_TEXT_SIZE-len(name+' - '+context[0])-1)+'\x1B[37;1m█\x1B[0m')
            add(f'\x1B[37;1m█\x1B[0m \x1B[34;1m{name}\x1B[37;1m - \x1B[;0m\x1b[;0m\x1B[35;1m{context[0]}\x1B[0m'+" "*(INSIDE_TEXT_SIZE-len(f'{name} - {context[0]}')-2)+' \x1B[37;1m█\x1B[0m') # Context[0] is command description
def start(start_menu='game'):
    try:
        if start_menu == 'game':
            game = Game().initialition_save()
        elif start_menu == 'save':
            game = Game().initialition_save()
            game.main()
    except ExitException:
        pass
    except KeyboardInterrupt:
        pass
    except ExitFromSaveException:
        start(start_menu='game')


if __name__ == '__main__':
    start(start_menu='save')
