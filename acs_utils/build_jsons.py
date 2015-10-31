# *_* coding: utf-8 *_*

import json
import os


def build_jsons():
    wep_dict = create_weapon_dictionary()
    directory = os.path.abspath(os.path.dirname(__file__))
    path = os.sep.join([directory, 'jsons', 'weapons.json'])
    dump_json(path, wep_dict)


def create_weapon_dictionary():
    wep_dict = {}

    # Empty weapon slot
    wname = 'empty weapon slot'
    pname = 'nothing'
    damage = 0
    cooldown = 10000
    range = 0
    accuracy = 0
    ammo = 0
    speed = 0
    wep_dict[wname] = make_dict(damage=damage, range=range,
                                cooldown=cooldown, acc=accuracy, ammo=ammo,
                                pname=pname, pspeed=speed)

    # Cannon
    wname = "cannon"
    pname = "cannon shell"
    damage = 10
    cooldown = 2
    range = 10
    accuracy = 0.25
    ammo = 200
    speed = 8
    wep_dict[wname] = make_dict(damage=damage, range=range,
                                cooldown=cooldown, acc=accuracy, ammo=ammo,
                                pname=pname, pspeed=speed)

    # Laser cannon
    wname = "laser cannon"
    pname = "laser beam"
    damage = 70
    cooldown = 12
    range = 21
    accuracy = 0.35
    ammo = 100
    speed = 1000
    wep_dict[wname] = make_dict(damage=damage, range=range,
                                cooldown=cooldown, acc=accuracy, ammo=ammo,
                                pname=pname, pspeed=speed)

    # Plasma cannon
    wname = "plasma cannon"
    pname = "plasma bolt"
    damage = 140
    cooldown = 12
    range = 52
    accuracy = 0.5
    ammo = 100
    speed = 1000
    wep_dict[wname] = make_dict(damage=damage, range=range,
                                cooldown=cooldown, acc=accuracy, ammo=ammo,
                                pname=pname, pspeed=speed)

    # Stringray launcher
    wname = "stingray launcher"
    pname = "stingray missile"
    damage = 70
    cooldown = 16
    range = 30
    accuracy = 0.7
    ammo = 6
    speed = 8
    wep_dict[wname] = make_dict(damage=damage, range=range,
                                cooldown=cooldown, acc=accuracy, ammo=ammo,
                                pname=pname, pspeed=speed)

    # Avalance launcher
    wname = "avalanche launcher"
    pname = "avalanche missile"
    damage = 100
    cooldown = 24
    range = 60
    accuracy = 0.8
    ammo = 3
    speed = 8
    wep_dict[wname] = make_dict(damage=damage, range=range,
                                cooldown=cooldown, acc=accuracy, ammo=ammo,
                                pname=pname, pspeed=speed)

    # Fusion ball launcher
    wname = "fusion ball launcher"
    pname = "fusion ball"
    damage = 230
    cooldown = 16
    range = 65
    accuracy = 1.0
    ammo = 2
    speed = 8
    wep_dict[wname] = make_dict(damage=damage, range=range,
                                cooldown=cooldown, acc=accuracy, ammo=ammo,
                                pname=pname, pspeed=speed)

    return wep_dict


def make_dict(**kwargs):
    """Converts a group of keyword arguments into a dictionary, i.e.:
    >>> foo = 'bar'; make_dict(baz=foo)
    {'baz': 'bar'}
    """
    new_dict = {}
    for key, value in kwargs.items():
        new_dict[key] = value

    return new_dict


def read_json(filename):
    """Attempts to read a json at filename."""
    with open(filename, 'r') as fd:
        return json.load(fd)


def dump_json(filename, data):
    """Dumps data to filename."""
    with open(filename, 'w') as fd:
        json.dump(data, fd)


# def equip_ufo_cannon(epower, ecooldown, erange, eacc):
#     """Return a "UFO cannon" Weapon object."""
#     ewname = "UFO cannon"
#     epname = "UFO cannon beam"
#     espeed = 10000
#     eammo = 10000
#     return UFOWeapon(wname=ewname, wdamage=epower, range=erange,
#                      wcooldown=ecooldown, wacc=eacc, wammo=eammo,
#                      pname=epname, pspeed=espeed)
#
# # pylint: disable=W0613
# def enc_sml_scout(dif):
#     """Return a "small scout" UFO."""
#     name = "small scout"
#     max_armor = 50
#     size = 1
#
#     return Craft(name_i=name, armor_i=max_armor, size_i=size,
#                  weplist=[equip_ufo_cannon(0, 2**64,
#                                            0, 0.0)])
#
# # pylint: enable=W0613
#
# def enc_med_scout(dif):
#     """Return a "medium scout" UFO."""
#     name = "medium scout"
#     max_armor = 200
#     size = 2
#     damage = 20
#     cooldown = 56
#     range = 15
#     accuracy = 0.6
#
#     return Craft(name_i=name, armor_i=max_armor, size_i=size,
#                  weplist=[equip_ufo_cannon(damage, cooldown,
#                                            range, accuracy)])
#
# def enc_lrg_scout(dif):
#     """Return a "large scout" UFO."""
#     name = "large scout"
#     max_armor = 250
#     size = 2
#     damage = 20
#     cooldown = 48
#     range = 34
#     accuracy = 0.6
#
#     return Craft(name_i=name, armor_i=max_armor, size_i=size,
#                  weplist=[equip_ufo_cannon(damage, cooldown,
#                                            range, accuracy)])
#
# def enc_abductor(dif):
#     """Return an "abductor" UFO."""
#     name = "abductor"
#     max_armor = 500
#     size = 3
#     damage = 40
#     cooldown = 48
#     range = 22
#     accuracy = 0.6
#
#     return Craft(name_i=name, armor_i=max_armor, size_i=size,
#                  weplist=[equip_ufo_cannon(damage, cooldown,
#                                            range, accuracy)])
#
# def enc_harvester(dif):
#     """Return a "harvester" UFO."""
#     name = "harvester"
#     max_armor = 500
#     size = 3
#     damage = 40
#     cooldown = 32
#     range = 20
#     accuracy = 0.6
#
#     return Craft(name_i=name, armor_i=max_armor, size_i=size,
#                  weplist=[equip_ufo_cannon(damage, cooldown,
#                                            range, accuracy)])
#
# def enc_supply_ship(dif):
#     """Return a "supply ship" UFO."""
#     name = "supply ship"
#     max_armor = 2200
#     size = 4
#     damage = 60
#     cooldown = 24
#     range = 36
#     accuracy = 0.6
#
#     return Craft(name_i=name, armor_i=max_armor, size_i=size,
#                  weplist=[equip_ufo_cannon(damage, cooldown,
#                                            range, accuracy)])
#
# def enc_terror_ship(dif):
#     """Return a "terror ship" UFO."""
#     name = "terror ship"
#     max_armor = 1200
#     size = 4
#     damage = 120
#     cooldown = 24
#     range = 42
#     accuracy = 0.6
#
#     return Craft(name_i=name, armor_i=max_armor, size_i=size,
#                  weplist=[equip_ufo_cannon(damage, cooldown,
#                                            range, accuracy)])
#
# def enc_battleship(dif):
#     """Return a "battleship" UFO."""
#     name = "battleship"
#     max_armor = 3000
#     size = 5
#     damage = 148
#     cooldown = 24
#     range = 65
#     accuracy = 0.6
#
#     return Craft(name_i=name, armor_i=max_armor, size_i=size,
#                  weplist=[equip_ufo_cannon(damage, cooldown,
#                                            range, accuracy)])


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    build_jsons()
