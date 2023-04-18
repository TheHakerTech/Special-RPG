# -*- coding: utf-8 -*-
class Event:
    def __init__(
        self,
        name: str,
        func: function,
        params: list or tuple | None
    ) -> None:
        self.name = name
        self.func = func
        self.params = params