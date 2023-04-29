# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import Callable
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
