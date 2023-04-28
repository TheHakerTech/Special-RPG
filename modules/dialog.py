# -*- coding: utf-8 -*-
from __future__ import annotations
class TypeDialog:
    text     = 'text'
    question = 'question'

class Dialog:
    def __init__(
        self,
        type: TypeDialog,
        text: list
    ) -> Dialog:
        self.type = type
        self.text = text


# format:
# Dialog(TypeDialog.text, text=[dialog1, dialogN])
# Dialog(TypeDialog.question, text=[<текст>, {'1':[[<текст1>, <текст2>], <функция>, <параметры к функции>]}])
