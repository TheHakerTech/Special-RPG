# -*- coding: utf-8 -*-
from modules.game_object import GameObject
# Main class for all items
class Item(GameObject):
    def __init__(
        self,
        name: str,
        description: str,
        interestring=None
    ) -> None:
        super().__init__(description, interestring)
        self.name = name

test_item = Item('Паяльник', 'Испорльзуется для паяния микросхем')