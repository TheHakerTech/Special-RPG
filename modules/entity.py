# -*- coding: utf-8 -*-
from modules.game_object import GameObject
# Dict entity.name:entity
entities = dict()
# Basic class for entities
class Entity(GameObject):
    def __init__(
        self,
        name: str,
        hp: int,
        items: list or tuple,
        description: str,
        interesting: str | None
    ) -> None:
        super().__init__(description, interestring=interesting)
        self.name = name
        self.hp = hp
        self.items = {k:v for (k, v) in zip([item.name for item in items], items)}
        self.full_hp = self.hp
        # Make new entity in entities
        entities[self.name] = self

class PlayableEntity(Entity):
    def __init__(self, name: str, hp: int, items: list or tuple, description: str, interesting: str | None) -> None:
        super().__init__(name, hp, items, description, interesting)
        # Too soon...
        
class NotPlayableEntity(Entity):
    def __init__(self, name: str, hp: int, items: list or tuple, description: str, interesting: str | None) -> None:
        super().__init__(name, hp, items, description, interesting)
        # Too soon...

class Player(Entity):
    def __init__(
        self,
        name: str,
        hp: int,
        items: list or tuple,
        description: str,
        interesting: str | None
    ) -> None:
        super().__init__(name, hp, items, description, interesting)


    