# -*- coding: utf-8 -*-
from modules.text import debug
# Class for every item/location/entity
class GameObject:
    def __init__(
        self,
        description: str,
        interesting: str | None
    ) -> None:
        self.description: str = description
        self.interesting: str | None = interesting
    
    def __doc__(self) -> None:
        return self.description
    
    def __setattr__(self, __name: str, __value) -> None:
        debug(f'Value of {self.__class__} changed: {__name} -> {__value}')
        self.__dict__[__name] = __value