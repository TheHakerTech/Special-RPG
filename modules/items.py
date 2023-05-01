# -*- coding: utf-8 -*-
from modules.game_object import GameObject
import modules.events as events
# Main class for all items
class Item(GameObject):
    def __init__(
        self,
        name: str,
        description: str,
        interestring=None,
        takeable=True,
        putable=True
    ) -> None:
        super().__init__(description, interestring)
        self.name = name
        self.takeable = takeable
        self.putable = putable
        self.events = {
            'OnReceived':events.NullEvent(),
            'OnTaken':events.NullEvent(),
            'OnPuten':events.NullEvent(),
            'OnUsen':events.NullEvent()
        }

test_item = Item('Паяльник', 'Испорльзуется для паяния микросхем')