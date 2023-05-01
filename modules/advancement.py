# -*- coding: utf-8 -*-
from __future__ import annotations
from modules.game_object import GameObject
class Advancement(GameObject):
    def __init__(
        self,
        name: str,
        description: str,
        status=False,
        interesting=''
    ) -> Advancement:
        super().__init__(description, interesting)
        self.name = name
        self.status = status

class Advancements(list):
    def __init__(
        self,
        _list=None
    ) -> Advancement:
        self.list = _list or []
        self.str_list = [str(adv) for adv in self.list]



advancements = Advancements([
    Advancement('test', 'test')
])