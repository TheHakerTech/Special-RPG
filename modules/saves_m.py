# -*- coding: utf-8 -*-
import pickle
import gzip
import modules.errors
import os
from os.path import exists
def saves():
    return [v[:-3] for v in os.listdir('saves/')]

def load_game(name):
    if exists(f'saves/{name}.gz'):
        with gzip.open(f'saves/{name}.gz', 'rb') as save_file:
            object = pickle.load(save_file)
        add_last_save(name)
        return object
    else:
        raise modules.errors.NoDefinedSaveError(f'No defined save {name}')
    
def delete(name):
    os.remove(f'saves/{name}.gz')

def save_game(name, object):
    with gzip.open(f'saves/{name}.gz', 'wb') as f:
        pickle.dump(object, f)
        add_last_save(name)

def add_last_save(name):
    with open('data/last_save.meta', 'w') as metafile:
        metafile.write(name)

def last_save_name():
    if exists('data/last_save.meta'):
        with open('data/last_save.meta', 'r') as metafile:
            result = metafile.read()
        if result != str():
            return result
        else:
            return None
    else:
        with open('data/last_save.meta', 'w') as metafile:
            pass
        last_save_name()