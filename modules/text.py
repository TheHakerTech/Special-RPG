# -*- coding: utf-8 -*-
from rich.console import Console
import time
import modules.errors
import os
# Init global variables
INSIDE_TEXT_SIZE = 69
INSIDE_TEXT_GAP = ' '*INSIDE_TEXT_SIZE

console = Console()
untimed_text = []
def delay_print(text, color, end='\n', delay=0.04, _add=False):
    for less in text:
        print(str(color)+less, end='', flush=True)
        time.sleep(delay)
    print('\033[0m'+end, end='')
    if _add:
        add(str(color)+text)

def add(text):
    debug(f'Added to untimed_text {text}')
    untimed_text.append(text)

def special_print(text, color, end='\n', delay=0.04, _add=False):
    if len(text) > INSIDE_TEXT_SIZE:
        raise modules.errors.MaxTextLimitedError("You limited max text len - >69")
    else:
        print('\x1B[37;1m█\x1B[0m ', end='')
        delay_print(text, '\x1B[35;1m', end='')
        print(' '*(INSIDE_TEXT_SIZE-len(text)-1), end='')
        print('\x1B[37;1m█\x1B[0m')
        if _add:
            add('\x1B[37;1m█\x1B[0m '+color+text+' '*(INSIDE_TEXT_SIZE-len(text)-1)+'\x1B[37;1m█\x1B[0m')

def redrow():
    os.system('cls||clear')
    for text in untimed_text:
        print(text)

def format_text_gap(text):
    return '\x1B[37;1m█\x1B[0m '+text+' '*(INSIDE_TEXT_SIZE-len(text)+22)+'\x1B[37;1m█\x1B[0m'

def debug(text):
    #console.log('[blue]DEBUG:[/blue]', text)
    pass
