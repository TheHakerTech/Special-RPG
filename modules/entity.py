# -*- coding: utf-8 -*-
from __future__ import annotations
from modules.game_object import GameObject
import modules.tools as tools
from modules.dialog import *
from modules.items import *
from modules.text import *
# Dict entity.name:entity
entities = dict()
# Basic class for entities
class Entity(GameObject):
    def __init__(
        self,
        name: str,
        hp: int,
        items: list or tuple,
        description: str,
        interesting: str | None
    ) -> None:
        super().__init__(description, interesting=interesting)
        self.name = name
        self.hp = hp
        if items != list():
            self.items: dict = {k:v for (k, v) in [(str(k2), v2) for (k2, v2) in enumerate(
                items,
                1
            )]}
        else:
            self.items = {}
        self.full_hp = self.hp
        # Make new entity in entities
        entities[self.name] = self
    
    def del_item(self, delete):
        tools.recreate_dict(self.items, delete)

class PlayableEntity(Entity):
    def __init__(self, name: str, hp: int, items: list or tuple, description: str, interesting: str | None) -> None:
        super().__init__(name, hp, items, description, interesting)
        # Too soon...
        
class NotPlayableEntity(Entity):
    def __init__(
        self,
        name: str,
        hp: int, 
        items: list or tuple,
        dialog: list,
        description: str,
        interesting=None
    ) -> PlayableEntity:
        super().__init__(name, hp, items, description, interesting)
        self.dialog: list = dialog

    def start_dialog(self):
        for dialog in self.dialog:
            if dialog.type == TypeDialog.text:
                for text in dialog.text:
                    print('\x1B[37;1m█\x1B[0m ', end='')
                    print(f'\x1B[36;1m{self.name}\x1B[;0m{":"} ', end='')
                    delay_print(f'{text}', '\x1B[35;1m', end='')
                    print(' '*(INSIDE_TEXT_SIZE-len(f'{self.name}: {text}')-1)+'\x1B[37;1m█\x1B[0m')
            elif dialog.type == TypeDialog.question:
                text: str = dialog.text[0] # Dialog
                answers = dict(dialog.text[1])
                # Print question
                print('\x1B[37;1m█\x1B[0m ', end='')
                print(f'\x1B[36;1m{self.name}\x1B[;0m{":"} ', end='')
                delay_print(f'{text}', '\x1B[;0m', end='')
                print(' '*(INSIDE_TEXT_SIZE-len(self.name+": "+text)-1))
                # Print player answers while answer is not emtpy
                while True:
                    # Print player answers
                    for _answer in answers.keys():
                        print('\x1B[37;1m█\x1B[0m ', end='')
                        print(f'\x1B[36;5m{_answer}\x1B[;0m - ', end='')
                        delay_print(f'{answers[_answer][0][0]}', '\x1B[36;1m', end='')
                        print(' '*(INSIDE_TEXT_SIZE-len(_answer+" - "+answers[_answer][0][0])-1), '\x1B[37;1m█\x1B[0m')
                    # Input player answer
                    answer = tools.controlled(lambda x: x in answers)
                    # Print answer
                    print('\x1B[37;1m█\x1B[0m ', end='')
                    print(f'\x1B[36;1m{self.name}\x1B[;0m{":"} ', end='')
                    delay_print(f'{answers[answer][0][1]}', '\x1B[;0m', end='')
                    print(' '*(INSIDE_TEXT_SIZE-len(self.name+": "+dialog.text[1][answer][0][0])-1))
                    tools.recreate_dict(answers, answer)
                    if answers == {}:
                        break
          
class Player(Entity):
    def __init__(
        self,
        name: str,
        hp: int,
        items: list or tuple,
        description: str,
        interesting: str | None
    ) -> None:
        super().__init__(name, hp, items, description, interesting)
        self.total_location = None # Current location
        self.total_think = 'Nothing' # Current dream
        self.spawnpoint = None # Current spawn

test_ent = NotPlayableEntity('Кэл', 100, [Item('asdasd', 'asdas')], [Dialog(TypeDialog.question, ['Сколько тебе лет?', {'1':[['54', 'Понял']], '2':[['34', 'Понял']]}])], 'asdasd')