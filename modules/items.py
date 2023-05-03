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

class ShopItem(Item):
    def __init__(
        self,
        name: str,
        description: str,
        cost,
        interestring=None, 
        takeable=True,
        putable=True
    ) -> None:
        super().__init__(name, description, interestring, takeable, putable)
        self.cost = cost
        self.item = Item(name, description, interestring, takeable=takeable, putable=putable)


test_item = Item('Паяльник', 'Испорльзуется для паяния микросхем')