# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import Callable

def _pass(): pass
class Event:
    def __init__(
        self,
        name: str,
        func: Callable,
        params=None
    ) -> Event:
        self.name: str = name
        self.func: Callable = func
        self.params = params or []

    def activate(self):
        self.func(*self.params)
class NullEvent:
    def __init__(self):
        self.name: str = 'NullEvent'
        self.func: Callable = _pass
        self.params = []
        
    def activate(self):
        self.func(*self.params)
