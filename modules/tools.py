# -*- coding: utf-8 -*-
import modules.entity as entity
import modules.advancement as adv
import modules.items as items

def give(ent, item: items.Item):
    ent.items[str(len(ent.items)+1)] = item
    item.events['OnReceived'].activate()
def putin_location(loc, item: items.Item):
    loc.items[str(len(loc.items)+1)] = item
def recreate_dict(dict: dict, delete):
    del dict[delete]
    c = dict.copy()
    dict.clear()
    dict.update({str(i): j for i, j in enumerate(c.values(),1)})
    return dict
def give_advancement(ent, advancement: adv):
    ent.maden_advancements.append(advancement)
    ent.events['OnAdvancement'].activate()
def controlled(check):
    # Допытываем пользователя, пока не сработает check
    while True:
        # Сохраняем позицию курсора
        print("\033[s", end="")
        print('\x1B[37;1m█\x1B[0m \x1B[35;1m-~>\x1B[;0m \x1B[31;1m', end='')
        result = input()
        if check(result):
            return result
        # Возвращаем курсор на место и чистим все, что под курсором
        print("\033[u\033[J", end="")