# -*- coding: utf-8 -*-
import json
import os.path

# Functions checking
def truefalse(arg):
    if arg.lower() in ['true', 'false']: return True
    else: return False
    
def isdigit(arg):
    result = False
    for a in arg:
        if a in [str(x) for x in range(1, 10)] or a in ['.', '0']:
            result = True
        else:
            return False
            break
    return result


settings = {
    'play_animation': ['true/false анимации текста','true'],
    'time': ['true/false счётчик времени игры','false'],
    'dev_mode': ['true/false задержки и анимации','false'],
    'delay':['number задержка анимаций',0.04],
    'debug':['true/false специальные принты','false']
}

settings_cheacking_funcs = {
    'play_animation':truefalse,
    'time':truefalse,
    'dev_mode':truefalse,
    'delay':isdigit,
    'debug':truefalse
}

default_settings = {
    'play_animation': ['true/false анимации текста','true'],
    'time': ['true/false счётчик времени игры','false'],
    'dev_mode': ['true/false задержки и анимации','false'],
    'delay':['number задержка анимаций',0.04],
    'debug':['true/false специальные принты','false']
}

def load_settings():
    global settings
    if not os.path.exists('data/settings.json'):
        update_settings()
    settings_file = open('data/settings.json', 'r') 
    settings = json.loads(settings_file.read())
    settings_file.close()

def update_settings():
    global settings
    if os.path.exists('data/settings.json'):
        settings_file = open('data/settings.json', 'w')
        settings_file.write(json.dumps(settings, skipkeys=True))
        settings_file.close()
    else:
        open('data/settings.json', 'w').close()
        update_settings()
load_settings()