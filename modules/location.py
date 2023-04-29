# -*- coding: utf-8 -*-
from __future__ import annotations
from modules.game_object import GameObject
import modules.tools as tools
import modules.events as events
class Location(GameObject):
    def __init__(
        self,
        name: str, # Name
        description: str,
        items=list(), # Вещи которые просто лежат в ней
        under_locs=list(),
        entities=list(),
        interesting=list(),
        intoable=True,
        exitable=True,
        parent=None
    ) -> Location:
        super().__init__(description, interesting)
        self.intoable = intoable # Can you into in this location
        self.exitable = exitable # Can you into in this location from it`s under location
        self.name: str = name # Name
        self.items = {str(k):v for (k, v) in [(str(k2), v2) for (k2, v2) in enumerate(items,1)]}
        self.under_locs: dict = {str(k):v for (k, v) in [(str(k2), v2) for (k2, v2) in enumerate(under_locs,1)]}
        self.entities: dict = {str(k):v for (k, v) in [(str(k2), v2) for (k2, v2) in enumerate(entities,1)]}
        self.parent = parent
        self.located = False
        # Events
        self.events = {
            'OnInto':events.NullEvent(),
            'OnLocated':events.NullEvent(),
            'OnExit':events.NullEvent()
        }

    def del_item(self, delete):
        tools.recreate_dict(self.items, delete)
    def del_entity(self, delete):
        tools.recreate_dict(self.entities, delete)
    def del_underloc(self, delete):
        tools.recreate_dict(self.under_locs, delete)
    def add(self, locs) -> Location:
        for location in locs:
            self.under_locs[str(len(self.under_locs)+1)] = location
            self.under_locs[str(len(self.under_locs))].parent = self
        return self
    
