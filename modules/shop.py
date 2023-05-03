# -*- coding: utf-8 -*-
from modules.text import *
import modules.tools as tools
from modules.currency import Currency as c

class Shop:
    def __init__(self, items: list):
        self.items = {str(num):name for (num, name) in enumerate(items, start=1)}
        
    def show(self):
        for (num, item) in self.items.items():
            print(f'\x1B[37;1m█\x1B[0m \x1B[34;1m{num}\x1b[;1m', end='')
            print('\x1B[37;1m - \x1B[;0m', end='')
            time.sleep(0.20)
            delay_print(item.name+' '+item.description, '\x1B[35;1m', end='')
            print(' '*(INSIDE_TEXT_SIZE-len(num+' - '+item.name+' '+item.description)-1)+'\x1B[37;1m█\x1B[0m')
           
        
    def buy(self, num):
        bought = self.items[num]
        tools.recreate_dict(self.items, num)
        special_print(f'Куплено: {bought.name}', '\x1B[34;1m')
        
        return bought