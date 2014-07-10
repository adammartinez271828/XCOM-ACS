# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 10:02:04 2014

@author: adam
"""

import numpy.random as nprand

# Static dictionary functions
def equip_empty():
    """Return an "empty" Weapon object."""
    wname = "empty weapon slot"
    pname = "nothing"
    return Weapon(wname, pname, 0, 0, 1000, 0, 0, 0)

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
    return Weapon(wname, pname, power, wrange, cooldown, speed,
                  accuracy, ammo)

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
    return Weapon(wname, pname, power, wrange, cooldown, speed,
                  accuracy, ammo)

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
    return Weapon(wname, pname, power, wrange, cooldown, speed,
                  accuracy, ammo)

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
    return Weapon(wname, pname, power, wrange, cooldown, speed,
                  accuracy, ammo)

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
    return Weapon(wname, pname, power, wrange, cooldown, speed,
                  accuracy, ammo)

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
    return Weapon(wname, pname, power, wrange, cooldown, speed,
                  accuracy, ammo)


def equip_ufo_cannon(power, cooldown, wrange, accuracy):
    """Return a "UFO cannon" Weapon object."""
    wname = "UFO cannon"
    pname = "UFO cannon beam"
    speed = 10000
    ammo = 10000
    return UFOWeapon(wname, pname, power, wrange, cooldown, speed,
                  accuracy, ammo)

def enc_sml_scout():
    """Return a "small scout" UFO."""
    name = "small scout"
    max_armor = 50
    size = 1

    return Craft(name, max_armor, size, equip_empty(),
                 equip_empty())

def enc_med_scout():
    """Return a "medium scout" UFO."""
    name = "medium scout"
    max_armor = 200
    size = 2
    damage = 20
    cooldown = 56
    wrange = 15
    accuracy = 0.6

    return Craft(name, max_armor, size,
                 equip_ufo_cannon(damage, cooldown, wrange, accuracy),
                 equip_empty())

def enc_lrg_scout():
    """Return a "large scout" UFO."""
    name = "large scout"
    max_armor = 250
    size = 2
    damage = 20
    cooldown = 48
    wrange = 34
    accuracy = 0.6

    return Craft(name, max_armor, size,
                 equip_ufo_cannon(damage, cooldown, wrange, accuracy),
                 equip_empty())

def enc_abductor():
    """Return an "abductor" UFO."""
    name = "abductor"
    max_armor = 500
    size = 3
    damage = 40
    cooldown = 48
    wrange = 22
    accuracy = 0.6

    return Craft(name, max_armor, size,
                 equip_ufo_cannon(damage, cooldown, wrange, accuracy),
                 equip_empty())

def enc_harvester():
    """Return a "harvester" UFO."""
    name = "harvester"
    max_armor = 500
    size = 3
    damage = 40
    cooldown = 32
    wrange = 20
    accuracy = 0.6

    return Craft(name, max_armor, size,
                 equip_ufo_cannon(damage, cooldown, wrange, accuracy),
                 equip_empty())

def enc_supply_ship():
    """Return a "supply ship" UFO."""
    name = "supply ship"
    max_armor = 2200
    size = 4
    damage = 60
    cooldown = 24
    wrange = 36
    accuracy = 0.6

    return Craft(name, max_armor, size,
                 equip_ufo_cannon(damage, cooldown, wrange, accuracy),
                 equip_empty())

def enc_terror_ship():
    """Return a "terror ship" UFO."""
    name = "terror ship"
    max_armor = 1200
    size = 4
    damage = 120
    cooldown = 24
    wrange = 42
    accuracy = 0.6

    return Craft(name, max_armor, size,
                 equip_ufo_cannon(damage, cooldown, wrange, accuracy),
                 equip_empty())

def enc_battleship():
    """Return a "battleship" UFO."""
    name = "battleship"
    max_armor = 3000
    size = 5
    damage = 148
    cooldown = 24
    wrange = 65
    accuracy = 0.6

    return Craft(name, max_armor, size,
                 equip_ufo_cannon(damage, cooldown, wrange, accuracy),
                 equip_empty())

def lnch_skyranger():
    """Return a "skyranger" craft."""
    name = "Skyranger"
    max_armor = 72

    return Craft(name, max_armor, 3, WEAPON_OPTIONS["empty"](),
                 WEAPON_OPTIONS["empty"]())

def lnch_interceptor(pwep="empty", swep="empty"):
    """Return an "interceptor" craft.

    Keyword arguments
    pwep -- the interceptor's primary weapon
    swep -- the interceptor's secondary weapon
    """
    name = "Interceptor"
    max_armor = 48

    return Craft(name, max_armor, 3, WEAPON_OPTIONS[pwep](),
                 WEAPON_OPTIONS[swep]())

def lnch_firestorm(pwep="empty", swep="empty"):
    """Return a "firestorm" craft.

    Keyword arguments
    pwep -- the interceptor's primary weapon
    swep -- the interceptor's secondary weapon
    """
    name = "Firestorm"
    max_armor = 240

    return Craft(name, max_armor, 3, WEAPON_OPTIONS[pwep](),
                 WEAPON_OPTIONS[swep]())

def lnch_lightning(pwep="empty"):
    """Return a "lightning" craft.

    Keyword arguments
    pwep -- the interceptor's primary weapon
    """
    name = "Lightning"
    max_armor = 384

    return Craft(name, max_armor, 3, WEAPON_OPTIONS[pwep](),
                 WEAPON_OPTIONS["empty"]())

def lnch_avenger(pwep="empty", swep="empty"):
    """Return an "avenger" craft.

    Keyword arguments
    pwep -- the interceptor's primary weapon
    swep -- the interceptor's secondary weapon
    """
    name = "Avenger"
    max_armor = 600

    return Craft(name, max_armor, 3, WEAPON_OPTIONS[pwep](),
                 WEAPON_OPTIONS[swep]())

# A list of all initialization options from ACS_Dictionary follow.
UFO_OPTIONS = {"small scout" : enc_sml_scout,
               "medium scout" : enc_med_scout,
               "large scout" : enc_lrg_scout,
               "abductor" : enc_abductor,
               "harvester" : enc_harvester,
               "supply ship" : enc_supply_ship,
               "terror ship" : enc_terror_ship,
               "battleship" : enc_battleship}

XC_CRAFT_OPTIONS = {"skyranger" : lnch_skyranger,
                    "interceptor" : lnch_interceptor,
                    "firestorm" : lnch_firestorm,
                    "lightning" : lnch_lightning,
                    "avenger" : lnch_avenger}

WEAPON_OPTIONS = {"empty" : equip_empty,
                  "cannon" : equip_cannon,
                  "laser cannon" : equip_laser_cannon,
                  "plasma cannon" : equip_plasma_cannon,
                  "stingray" : equip_stingray,
                  "avalanche" : equip_avalanche,
                  "fbl" : equip_fbl}

DIFFICULTY_OPTIONS = {"beginner" : 1,
                      "experienced" : 2,
                      "veteran" : 3,
                      "genius" : 4,
                      "superhuman" : 5}
                      
ATTACK_MODE_OPTIONS = {"aggressive" : 1,
                       "standard" : 2,
                       "cautious" : 3}

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
        if dist == None:
            self.distance -= self.weapon.projectile_speed
        else:
            self.distance -= dist
        if self.distance <= 0:
            return True
        return False

class Weapon(object):
    """This is a Weapon object."""

    def __init__(self, name="empty weapon slot", aname="nothing", pdamage=0,
                 wrange=0, cooldown=1000, pspeed=0, acc=0.0,
                 ammo=0):
        """Instantiate a Weapon object.

        Keyword arguments
        name -- the name of the Weapon
        wrange -- the maximum firing range of the Weapon
        cooldown -- the cooldown time (in ticks) before the weapon can fire
            again
        acc -- the Weapon's base accuracy
        ammo -- the Weapon's maximum ammunition capacity
        pname -- the name of the Weapon's Projectile
        pdamage -- the damage the Weapon's Projectile deals
        pspeed -- the travel speed of the Weapon's Projectile
        """

        self.weapon_name = name
        self.ammo_name = aname
        self.damage = pdamage
        self.max_range = wrange
        self.cooldown = cooldown
        self.projectile_speed = pspeed
        self.accuracy = acc
        self.ammo_capacity = ammo

        self.current_ammo = ammo
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
        """Determine if the weapon is ready to fire and has a firing solution.

        Arguments
        {0} -- distance to target
        """
        if (self.cooldown_timer <= 0 and current_range <= self.max_range and
                self.current_ammo > 0):
            return True
        return False

    def fire(self, target, current_range):
        """Fire a projectile if the Weapon is in a ready status.

        Arguments
        {0} -- distance to target
        {1} -- target
        """
        if self.is_ready_to_fire(current_range):
            self.cooldown_timer = self.cooldown
            self.current_ammo -= 1
            return Projectile(self, target, current_range)
        return None

class UFOWeapon(Weapon):
    """This is a Weapon for a UFO."""
        
    
    def fire(self, target, current_range, difficulty):
        """Fire a projectile if the Weapon is in a ready status.

        Arguments
        {0} -- distance to target
        {1} -- target
        {2} -- game difficulty
        """
        if self.is_ready_to_fire(current_range):
            self.cooldown_timer = int(round((1+nprand.random()) * \
                                  (self.cooldown-2*difficulty)))
            self.current_ammo -= 1
#            print("The UFOWeapon will require {0}s to recharge.".format(self.cooldown_timer))
            return Projectile(self, target, current_range)
        return None
        
class Craft(object):
    """This is a Craft object."""

    def __init__(self, name_i="", armor_i=0, size_i=0,
                 pwep_i=equip_empty(),
                 swep_i=equip_empty()):
        """Instantiate a Craft object.

        Keyword arguments
        name -- the name string of the craft
        armor -- the maximum armor of the craft
        size -- the size factor of the craft
        pwep -- a Weapon object for the craft's primary weapon slot
        swep -- a Weapon object for the craft's secondary weapon slot
        """
        self.name = name_i
        self.max_armor = armor_i
        self.primary_weapon = pwep_i
        self.secondary_weapon = swep_i

        self.current_armor = self.max_armor
        self.dodge_multiplier = (1 + 3.0/(6-size_i)) / 2

    def take_damage(self, boom=0):
        """Adjust the Craft's armor and return the result.

        Keyword arguments
        boom -- the damage the craft has taken
        """
        self.current_armor -= boom
        return self.current_armor

    def reset(self):
        """Reset the craft to its initial state."""
        self.current_armor = self.max_armor
        self.primary_weapon.reset()
        self.secondary_weapon.reset()

    def tick(self):
        """Tick the Craft's weapons."""
        self.primary_weapon.tick()
        self.secondary_weapon.tick()
