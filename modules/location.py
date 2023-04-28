# -*- coding: utf-8 -*-
from __future__ import annotations
from modules.game_object import GameObject
import modules.tools as tools
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
        if items != list():
            self.items: dict = {str(k):v for (k, v) in [(str(k2), v2) for (k2, v2) in enumerate(
                items,
                1
            )]}
        else:
            self.items = {}
        if under_locs != list():
            self.under_locs: dict = {str(k):v for (k, v) in [(str(k2), v2) for (k2, v2) in enumerate(
                under_locs,
                1
            )]}
        else:
            self.under_locs = {}
        if entities != list():
            self.entities: dict = {str(k):v for (k, v) in [(str(k2), v2) for (k2, v2) in enumerate(
                entities,
                1
            )]}
        else:
            self.entities = {}
        self.parent = parent

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