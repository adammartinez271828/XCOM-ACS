# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 21:10:34 2014

@author: adam
"""

import sys
import random
import acs_module as acsm

# Runs a collection of simulations ("Combats") of an XCOM air combat
# The interceptor is presumed to engage in an aggressive assault starting from
#  standoff.
# The interceptor will close distance to 5km.
# The UFO will not attempt escape.
# Craft close distance at a rate of .5km/gs.
# Combat will continue until one or both ships are destroyed.
# All times are measured in game seconds.
# All distances are measured in kilometers.

class AirCombatSimulation(object):
    """This is an Air Combat Simulation object."""

    # class variables
    craft_approach_rate = 0.5 # 0.5km/gs
    craft_fallback_rate = 0.5 # 0.5km/gs
    standoff_dist = 70

    def __init__(self, ufo="small scout", interceptor="interceptor",
                 pwt="empty", swt="empty", dif=1, atkmode=1):
        """Instantiate an Air Combat Simulation object.

        Keyword arguments
        ufo -- ufo type
        interceptor -- interceptor type
        pwt -- interceptor's primary weapon type
        swt -- interceptor's secondary weapon type
        dif -- game difficulty setting
        atkmode -- interceptor's attack mode
        """
        self.ufo = acsm.UFO_OPTIONS[ufo]()
        self.interceptor = acsm.XC_CRAFT_OPTIONS[interceptor](pwt, swt)
        self.difficulty = acsm.DIFFICULTY_OPTIONS[dif]
        self.attackmode = atkmode

        # Set minimum distance and adjust interceptor's missile cooldown for
        #     attack mode
        if self.attackmode == "aggressive":
            self.min_dist = 5
        elif self.attackmode == "standard":
            self.min_dist = min(self.interceptor.primary_weapon.max_range,
                                self.interceptor.secondary_weapon.max_range)
            if not "cannon" in self.interceptor.primary_weapon.weapon_name:
                self.interceptor.primary_weapon.cooldown = \
                    int(round(self.interceptor.primary_weapon.cooldown * 1.5))
            if not "cannon" in self.interceptor.secondary_weapon.weapon_name:
                self.interceptor.secondary_weapon.cooldown = \
                    int(round(self.interceptor.secondary_weapon.cooldown * 1.5))
        else:
            self.min_dist = max(self.interceptor.primary_weapon.max_range,
                                self.interceptor.secondary_weapon.max_range)
            if not "cannon" in self.interceptor.primary_weapon.weapon_name:
                self.interceptor.primary_weapon.cooldown = \
                    self.interceptor.primary_weapon.cooldown * 2
            if not "cannon" in self.interceptor.secondary_weapon.weapon_name:
                self.interceptor.secondary_weapon.cooldown = \
                    self.interceptor.secondary_weapon.cooldown * 2

        # Initialize some variables
        self.crashpoint = .5*self.ufo.max_armor
        self.initialize()

    def initialize(self):
        """Initalize the air combat for another round."""
        self.clock = 0
        self.dist = AirCombatSimulation.standoff_dist
        self.proj_list = list()
        self.interceptor.reset()
        self.ufo.reset()

    def run_combat(self):
        """Run a single combat.

        Return the end state of the combat.
        """
        self.initialize()

        while (self.interceptor.current_armor > 0 and
               self.ufo.current_armor > self.crashpoint):

            # Iterate clock
            self.clock += 1
            if self.clock > 1000000:
                sys.exit("Maximum allowable time exceeded.  Quitting...")

            # Let missiles fly
            for proj in self.proj_list[:]:
                if proj.fly():
                    if (random.random() < proj.weapon.accuracy * \
                        proj.target.dodge_multiplier):
                        if proj.target == self.ufo:
                            # Deals 50%-100% damage
                            boom = int(round((1+random.random())/2 *
                                             proj.weapon.damage))
                        else:
                            # Deals 0%-100% damage
                            boom = int(round(random.random() *
                                             proj.weapon.damage))
                        proj.target.take_damage(boom)
#                        print("The {0} takes {1} damage from a {2} at {3}s." \
#                              .format(proj.target.name, boom, \
#                              proj.weapon.ammo_name, self.clock))
#                    else:
#                        print("The {0} misses the {1} at {2}s.".format( \
#                              proj.weapon.ammo_name, proj.target.name, \
#                              self.clock))
                    self.proj_list.remove(proj)
#                else: print("The {0} sails through the air.".format( \
#                            proj.weapon.ammo_name))

            # Move craft
            if self.dist > self.min_dist:
                self.dist -= AirCombatSimulation.craft_approach_rate
            elif self.dist < self.min_dist:
                self.dist += AirCombatSimulation.craft_fallback_rate

            # Tick weapons
            self.ufo.tick()
            self.interceptor.tick()

            # Fire UFO Weapons
            if self.ufo.primary_weapon.is_ready_to_fire(self.dist):
                self.proj_list.append(
                    self.ufo.primary_weapon.fire(self.interceptor, self.dist,
                                                 self.difficulty))
#                print("The {0} fires its {1} at {2}s.".format(self.ufo.name, \
#                      self.ufo.primary_weapon.weapon_name, self.clock))

            # Fire Interceptor Weapons
            if self.interceptor.primary_weapon.is_ready_to_fire(self.dist):
                self.proj_list.append(
                    self.interceptor.primary_weapon.fire(self.ufo, self.dist))
#                print("The {0} fires its {1} at {2}s.".format( \
#                      self.interceptor.name, \
#                      self.interceptor.primary_weapon.weapon_name, \
#                      self.clock))

            if self.interceptor.secondary_weapon.is_ready_to_fire(self.dist):
                self.proj_list.append(
                    self.interceptor.secondary_weapon.fire(self.ufo, self.dist))
#                print("The {0} fires its {1} at {2}s.".format( \
#                      self.interceptor.name, \
#                      self.interceptor.secondary_weapon.weapon_name, \
#                      self.clock))

            # Interceptor breaks off if it runs out of ammo
            if (self.interceptor.primary_weapon.current_ammo == 0 and
                self.interceptor.secondary_weapon.current_ammo == 0):
                break

        """ Determine final state of simulation and return binary value.
            0 -- ufo escaped
            1 -- interceptor destroyed
            2 -- ufo destroyed
            3 -- interceptor destroyed, ufo destroyed
            4 -- ufo crashed
            5 -- interceptor destroyed, ufo crashed
        """
        final_state = 0b000
        if self.interceptor.current_armor <= 0:
            final_state += 0b001
        if self.ufo.current_armor <= 0:
            final_state += 0b010
        elif self.ufo.current_armor <= self.crashpoint:
            final_state += 0b100

        return {"result" : final_state}

class main(object):
    """Run on execution of Combat.py."""
    result_table = ["interceptor rtb, ufo escaped",
                    "interceptor destroyed, ufo escaped",
                    "interceptor rtb, ufo destroyed",
                    "interceptor destroyed, ufo destroyed",
                    "interceptor rtb, ufo crashed",
                    "interceptor destroyed, ufo crashed"]
    result_tally = [0,0,0,0,0,0]

    combat = AirCombatSimulation(ufo="harvester", interceptor="avenger",
                                 pwt="avalanche", swt="avalanche",
                                 dif="superhuman",
                                 atkmode="standard")

    for i in range(1000):
        combat.initialize()
        result = combat.run_combat()
        result_tally[result["result"]] += 1

    print ""
    print "Interceptor is a {0} equipped with a {1} and a {2}.".format( \
        combat.interceptor.name, \
        combat.interceptor.primary_weapon.weapon_name, \
        combat.interceptor.secondary_weapon.weapon_name)
    print ""
    print "UFO is a {0} equipped with a {1}.".format( \
        combat.ufo.name, \
        combat.ufo.primary_weapon.weapon_name)
    print ""
    print ("Difficulty was set to {0} and the ".format(combat.difficulty) +
        "interceptor was set to {0} attack mode.".format(combat.attackmode))
    print ""
    print "Results:"
    for i in range(6):
        print "{0}: {1}".format(result_table[i], result_tally[i])
    print ""

if __name__ == "__main__":
    main()
