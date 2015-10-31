# -*- coding: utf-8 -*-
"""
Utilities module for xcomacs.
"""

import json
import random


def load_json(filename):
    with open(filename) as fd:
        return json.load(fd)


# Static dictionary functions
def equip_empty():
    """Return an "empty" Weapon object."""
    wname = "empty weapon slot"
    pname = "nothing"
    return Weapon(wname=wname, wdamage=0, wrange=0,
                  wcooldown=10000, wacc=0, wammo=0,
                  pname=pname, pspeed=0)


def equip_cannon():
    """Return a "cannon" Weapon object."""
    wname = "cannon"
    pname = "cannon shell"
    power = 10
    cooldown = 2
    wrange = 10
    accuracy = 0.25
    ammo = 200
    speed = 8
    return Weapon(wname=wname, wdamage=power, wrange=wrange,
                  wcooldown=cooldown, wacc=accuracy, wammo=ammo,
                  pname=pname, pspeed=speed)


def equip_laser_cannon():
    """Return a "laser cannon" Weapon object."""
    wname = "laser cannon"
    pname = "laser beam"
    power = 70
    cooldown = 12
    wrange = 21
    accuracy = 0.35
    ammo = 100
    speed = 1000
    return Weapon(wname=wname, wdamage=power, wrange=wrange,
                  wcooldown=cooldown, wacc=accuracy, wammo=ammo,
                  pname=pname, pspeed=speed)


def equip_plasma_cannon():
    """Return a "plasma cannon" Weapon object."""
    wname = "plasma cannon"
    pname = "plasma bolt"
    power = 140
    cooldown = 12
    wrange = 52
    accuracy = 0.5
    ammo = 100
    speed = 1000
    return Weapon(wname=wname, wdamage=power, wrange=wrange,
                  wcooldown=cooldown, wacc=accuracy, wammo=ammo,
                  pname=pname, pspeed=speed)


def equip_stingray():
    """Return a "stingray launcher" Weapon object."""
    wname = "stingray launcher"
    pname = "stingray missile"
    power = 70
    cooldown = 16
    wrange = 30
    accuracy = 0.7
    ammo = 6
    speed = 8
    return Weapon(wname=wname, wdamage=power, wrange=wrange,
                  wcooldown=cooldown, wacc=accuracy, wammo=ammo,
                  pname=pname, pspeed=speed)


def equip_avalanche():
    """Return an "avalanche launcher" Weapon object."""
    wname = "avalanche launcher"
    pname = "avalanche missile"
    power = 100
    cooldown = 24
    wrange = 60
    accuracy = 0.8
    ammo = 3
    speed = 8
    return Weapon(wname=wname, wdamage=power, wrange=wrange,
                  wcooldown=cooldown, wacc=accuracy, wammo=ammo,
                  pname=pname, pspeed=speed)


def equip_fbl():
    """Return a "fusion ball launcher" Weapon object."""
    wname = "fusion ball launcher"
    pname = "fusion ball"
    power = 230
    cooldown = 16
    wrange = 65
    accuracy = 1.0
    ammo = 2
    speed = 8
    return Weapon(wname=wname, wdamage=power, wrange=wrange,
                  wcooldown=cooldown, wacc=accuracy, wammo=ammo,
                  pname=pname, pspeed=speed)


def equip_ufo_cannon(epower, ecooldown, erange, eacc):
    """Return a "UFO cannon" Weapon object."""
    ewname = "UFO cannon"
    epname = "UFO cannon beam"
    espeed = 10000
    eammo = 10000
    return UFOWeapon(wname=ewname, wdamage=epower, wrange=erange,
                     wcooldown=ecooldown, wacc=eacc, wammo=eammo,
                     pname=epname, pspeed=espeed)


def enc_sml_scout():
    """Return a "small scout" UFO."""
    name = "small scout"
    max_armor = 50
    size = 1

    return Craft(name_i=name, armor_i=max_armor, size_i=size,
                 weplist=[equip_ufo_cannon(0, 2**64,
                                           0, 0.0)])


def enc_med_scout():
    """Return a "medium scout" UFO."""
    name = "medium scout"
    max_armor = 200
    size = 2
    damage = 20
    cooldown = 56
    wrange = 15
    accuracy = 0.6

    return Craft(name_i=name, armor_i=max_armor, size_i=size,
                 weplist=[equip_ufo_cannon(damage, cooldown,
                                           wrange, accuracy)])


def enc_lrg_scout():
    """Return a "large scout" UFO."""
    name = "large scout"
    max_armor = 250
    size = 2
    damage = 20
    cooldown = 48
    wrange = 34
    accuracy = 0.6

    return Craft(name_i=name, armor_i=max_armor, size_i=size,
                 weplist=[equip_ufo_cannon(damage, cooldown,
                                           wrange, accuracy)])


def enc_abductor():
    """Return an "abductor" UFO."""
    name = "abductor"
    max_armor = 500
    size = 3
    damage = 40
    cooldown = 48
    wrange = 22
    accuracy = 0.6

    return Craft(name_i=name, armor_i=max_armor, size_i=size,
                 weplist=[equip_ufo_cannon(damage, cooldown,
                                           wrange, accuracy)])


def enc_harvester():
    """Return a "harvester" UFO."""
    name = "harvester"
    max_armor = 500
    size = 3
    damage = 40
    cooldown = 32
    wrange = 20
    accuracy = 0.6

    return Craft(name_i=name, armor_i=max_armor, size_i=size,
                 weplist=[equip_ufo_cannon(damage, cooldown,
                                           wrange, accuracy)])


def enc_supply_ship():
    """Return a "supply ship" UFO."""
    name = "supply ship"
    max_armor = 2200
    size = 4
    damage = 60
    cooldown = 24
    wrange = 36
    accuracy = 0.6

    return Craft(name_i=name, armor_i=max_armor, size_i=size,
                 weplist=[equip_ufo_cannon(damage, cooldown,
                                           wrange, accuracy)])


def enc_terror_ship():
    """Return a "terror ship" UFO."""
    name = "terror ship"
    max_armor = 1200
    size = 4
    damage = 120
    cooldown = 24
    wrange = 42
    accuracy = 0.6

    return Craft(name_i=name, armor_i=max_armor, size_i=size,
                 weplist=[equip_ufo_cannon(damage, cooldown,
                                           wrange, accuracy)])


def enc_battleship():
    """Return a "battleship" UFO."""
    name = "battleship"
    max_armor = 3000
    size = 5
    damage = 148
    cooldown = 24
    wrange = 65
    accuracy = 0.6

    return Craft(name_i=name, armor_i=max_armor, size_i=size,
                 weplist=[equip_ufo_cannon(damage, cooldown,
                                           wrange, accuracy)])


def lnch_skyranger(weplist, atkmode):
    """Return a "skyranger" craft.

    Positional arguments
    {0} -- a List of keys for the Craft's Weapons
    {1} -- the Craft's attack mode
    """
    name = "Skyranger"
    max_armor = 72

    weapons = []
    for wep in weplist:
        weapons.append(WEAPON_OPTIONS[wep]())

    return Craft(name_i=name, armor_i=max_armor,
                 weplist=weapons, atkmode_i=atkmode)


def lnch_interceptor(weplist, atkmode):
    """Return an "interceptor" craft.

    Positional arguments
    {0} -- a List of keys for the Craft's Weapons
    {1} -- the Craft's attack mode
    """
    name = "Interceptor"
    max_armor = 48

    weapons = []
    for wep in weplist:
        weapons.append(WEAPON_OPTIONS[wep]())

    return Craft(name_i=name, armor_i=max_armor,
                 weplist=weapons, atkmode_i=atkmode)


def lnch_firestorm(weplist, atkmode):
    """Return a "firestorm" craft.

    Positional arguments
    {0} -- a List of keys for the Craft's Weapons
    {1} -- the Craft's attack mode
    """
    name = "Firestorm"
    max_armor = 240

    weapons = []
    for wep in weplist:
        weapons.append(WEAPON_OPTIONS[wep]())

    return Craft(name_i=name, armor_i=max_armor,
                 weplist=weapons, atkmode_i=atkmode)


def lnch_lightning(weplist, atkmode):
    """Return a "lightning" craft.

    Positional arguments
    {0} -- a List of keys for the Craft's Weapons
    {1} -- the Craft's attack mode
    """
    name = "Lightning"
    max_armor = 384

    weapons = []
    for wep in weplist:
        weapons.append(WEAPON_OPTIONS[wep]())

    return Craft(name_i=name, armor_i=max_armor,
                 weplist=weapons, atkmode_i=atkmode)


def lnch_avenger(weplist, atkmode):
    """Return an "avenger" craft.

    Positional arguments
    {0} -- a List of keys for the Craft's Weapons
    {1} -- the Craft's attack mode
    """
    name = "Avenger"
    max_armor = 600

    weapons = []
    for wep in weplist:
        weapons.append(WEAPON_OPTIONS[wep]())

    return Craft(name_i=name, armor_i=max_armor,
                 weplist=weapons, atkmode_i=atkmode)


# A list of all initialization options follow.
UFO_OPTIONS = {"small scout": enc_sml_scout,
               "medium scout": enc_med_scout,
               "large scout": enc_lrg_scout,
               "abductor": enc_abductor,
               "harvester": enc_harvester,
               "supply ship": enc_supply_ship,
               "terror ship": enc_terror_ship,
               "battleship": enc_battleship}

XC_CRAFT_OPTIONS = {"skyranger": lnch_skyranger,
                    "interceptor": lnch_interceptor,
                    "firestorm": lnch_firestorm,
                    "lightning": lnch_lightning,
                    "avenger": lnch_avenger}

WEAPON_OPTIONS = {"empty": equip_empty,
                  "cannon": equip_cannon,
                  "laser cannon": equip_laser_cannon,
                  "plasma cannon": equip_plasma_cannon,
                  "stingray": equip_stingray,
                  "avalanche": equip_avalanche,
                  "fbl": equip_fbl}

DIFFICULTY_OPTIONS = {"beginner": 1,
                      "experienced": 2,
                      "veteran": 3,
                      "genius": 4,
                      "superhuman": 5}


class Projectile(object):
    """This is a Projectile object."""

    def __init__(self, weapon, target, distance):
        """Instantiate a Projectile object.

        Positional arguments:
        {0} -- the Weapon the Projectile came from
        {1} -- the Projectile's target
        {2} -- the distance from the Projectile to the Target
        """
        self.weapon = weapon
        self.target = target
        self.distance = distance

    def fly(self, dist=None):
        """Move the Projectile. Defaults to the Projectile's speed.

        Returns True when the projectile reaches the target.

        Keyword arguments
        dist -- distance the Projectile moves TOWARD the target.
        """
        if dist is None:
            self.distance -= self.weapon.projectile_speed
        else:
            self.distance -= dist
        if self.distance <= 0:
            return True
        return False


class Weapon(object):
    """This is a Weapon object."""

    def __init__(self, wname="empty weapon slot", wdamage=0,
                 wrange=0, wcooldown=1000, wacc=0.0, wammo=0,
                 pname="nothing", pspeed=0):
        """Instantiate a Weapon object.

        Keyword arguments
        wname -- the wname of the Weapon
        wdamage -- the damage the Weapon deals
        wrange -- the maximum firing range of the Weapon
        wcooldown -- the cooldown time (in ticks) before the weapon can fire
            again
        wacc -- the Weapon's base accuracy
        wammo -- the Weapon's maximum ammunition capacity
        pname -- the name of the Weapon's Projectile
        pspeed -- the travel speed of the Weapon's Projectile
        """
        self.weapon_name = wname
        self.damage = wdamage
        self.max_range = wrange
        self.cooldown = wcooldown
        self.accuracy = wacc
        self.ammo_capacity = wammo

        self.projectile_name = pname
        self.projectile_speed = pspeed

        self.current_ammo = self.ammo_capacity
        self.cooldown_timer = 0

    def reset(self):
        """Reset the Weapon to default state."""
        self.current_ammo = self.ammo_capacity
        self.cooldown_timer = 0

    def tick(self, time=1):
        """Notify the weapon that time has passed.

        Defaults to 1 tick.

        Keyword arguments
        time -- number of ticks that have passed
        """
        self.cooldown_timer -= time

    def is_ready_to_fire(self, current_range):
        """Return True if the weapon is ready to fire and target is in range.

        Arguments
        {0} -- distance to target
        """
        if (self.cooldown_timer <= 0 and current_range <= self.max_range and
                self.current_ammo > 0):
            return True
        return False

    def fire(self, target, current_range):
        """Fire a projectile.

        Does not check ready status or ammunition count.

        Arguments
        {0} -- distance to target
        {1} -- target
        """
        self.cooldown_timer = self.cooldown
        self.current_ammo -= 1
        return Projectile(self, target, current_range)


class UFOWeapon(Weapon):
    """This is a Weapon for a UFO."""

    def fire(self, target, current_range):
        """Fire a projectile if the Weapon is in a ready status.

        Does not check ready status or ammunition count.

        Arguments
        {0} -- distance to target
        {1} -- target
        """
        # UFOs have from 100% to 200% of adjusted cooldown per shot.
        self.cooldown_timer = int(round((1 + random.random()) * self.cooldown))
        # UFOs have unlimted ammo!
        # self.current_ammo -= 1
        return Projectile(self, target, current_range)


class Craft(object):
    """This is a Craft object."""

    def __init__(self, name_i="", armor_i=0, size_i=3,
                 weplist=None, atkmode_i="standard"):
        """Instantiate a Craft object.

        Keyword arguments
        name_i -- the name string of the craft
        armor_i -- the maximum armor of the craft
        weplist -- a list of Weapon objects
        size_i -- the size factor of the craft
        atkmode_i -- the craft's mode of attack
        """
        self.name = name_i
        self.max_armor = armor_i
        if weplist is None:
            self.weapons = []
        else:
            self.weapons = weplist
        # Effectively unused by XCOM: default size craft have a mult of 1
        self.dodge_multiplier = (1 + 3.0/(6-size_i)) / 2
        # Unused by UFOs
        self.attack_mode = atkmode_i

        # Adjust cooldowns for attack mode.
        # Will have no effect on UFO-type weapons
        for wep in self.weapons:
            if "cannon" not in wep.weapon_name:
                if self.attack_mode == "standard":
                    wep.cooldown = int(round(wep.cooldown * 1.5))
                elif self.attack_mode == "cautious":
                    wep.cooldown *= 2

        self.current_armor = self.max_armor
        self.distance_to_target = 2**64

        # Find craft's preferred distances.
        # For UFO craft, standard/cautious is optimal engagement range.
        self._preferred_distance = {"aggressive": 5,
                                    "standard": 1000,
                                    "cautious": 0}
        for wep in self.weapons:
            if wep.max_range < self._preferred_distance["standard"]:
                self._preferred_distance["standard"] = wep.max_range
            if wep.max_range > self._preferred_distance["cautious"]:
                self._preferred_distance["cautious"] = wep.max_range

    def adjust_cooldown(self, ticks):
        """Flat adjust all weapon cooldowns.

        Used to set difficulty cooldown reduction on UFOs.

        Positional arguments
        {0} -- number of seconds to reduce weapon cooldown
        """
        for wep in self.weapons:
            wep.cooldown -= ticks

    @property
    def preferred_distance(self):
        """Return the craft's preferred engagement distance.

        Determined by weapon selection and attack mode.
        """
        return self._preferred_distance[self.attack_mode]

    def take_damage(self, boom=0):
        """Adjust the Craft's armor and return the result.

        Keyword arguments
        boom -- damage the craft has taken
        """
        self.current_armor -= boom
        return self.current_armor

    def reset(self):
        """Reset the Craft to its initial state."""
        self.current_armor = self.max_armor
        for wep in self.weapons:
            wep.reset()

    def tick(self):
        """Tick the Craft's weapons."""
        for wep in self.weapons:
            wep.tick()
