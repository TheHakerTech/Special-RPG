# -*- coding: utf-8 -*-
from modules.text import debug
from typing import Callable
import modules.events as events
# Class for every item/location/entity
class GameObject:
    def __init__(
        self,
        description: str,
        interesting: str | None
    ) -> None:
        self.description: str = description
        self.interesting: str | None = interesting
        self.events = {
            'TestEvent':None
        }
    
    def __doc__(self) -> None:
        return self.description
    
    def __setattr__(self, __name: str, __value) -> None:
        debug(f'Value of {self.__class__} changed: {__name} -> {__value}')
        self.__dict__[__name] = __value
    
    def bind(self, evt_name: str, evt_func: Callable, func_params=None):
        self.events[evt_name] = events.Event(evt_name, evt_func, func_params)