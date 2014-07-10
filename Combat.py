# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 21:10:34 2014

@author: adam
"""

import numpy.random as nprand
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
    craft_dist_close_rate = 0.5 # 0.5km/gs
    standoff_dist = 70
    min_dist = 5

    def __init__(self, ufo="small scout", interceptor="interceptor",
                 pwt="empty", swt="empty", dif=1):
        """Instantiate an Air Combat Simulation object.

        Keyword arguments
        ufo -- ufo type
        interceptor -- interceptor type
        pwt -- interceptor's primary weapon type
        swt -- interceptor's secondary weapon type
        dif -- game difficulty setting
        """
        self.ufo = acsm.UFO_OPTIONS[ufo]()
        self.interceptor = acsm.XC_CRAFT_OPTIONS[interceptor](pwt, swt)
        self.difficulty = acsm.DIFFICULTY_OPTIONS[dif]

        self.crashpoint = .5*self.ufo.max_armor
        self.clock = 0
        self.dist = AirCombatSimulation.standoff_dist
        self.proj_list = list()

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

        while (self.interceptor.current_armor > 0 and self.ufo.current_armor >
               self.crashpoint):
            # Iterate clock
            self.clock += 1

            # Let missiles fly
            for proj in self.proj_list[:]:
                if proj.fly():
                    if (nprand.random() < proj.weapon.accuracy * \
                        proj.target.dodge_multiplier):
                        if proj.target == self.ufo:
                            # Deals 50%-100% damage
                            boom = int(round((1+nprand.random())/2 *
                                             proj.weapon.damage))
                        else:
                            # Deals 0%-100% damage
                            boom = int(round(nprand.random() *
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
            if self.dist > AirCombatSimulation.min_dist:
                self.dist -= AirCombatSimulation.craft_dist_close_rate

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
#                      self.interceptor.primary_weapon.weapon_name, \
#                      self.clock))

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
            
        return {"result" : final_state,
#                "int obj" : self.interceptor,
#                "ufo obj" : self.ufo
                }
            
class main(object):
    """Run on execution of Combat.py."""
    result_table = ["interceptor rtb, ufo escaped",                    
                    "interceptor destroyed, ufo escaped",
                    "interceptor rtb, ufo destroyed",
                    "interceptor destroyed, ufo destroyed",
                    "interceptor rtb, ufo crashed",
                    "interceptor destroyed, ufo crashed"]
    result_tally = [0,0,0,0,0,0]
    
    combat = AirCombatSimulation(ufo="battleship", interceptor="avenger",
                                 pwt="fbl", swt="plasma cannon", dif="superhuman")

    for i in range(1000):
        combat.initialize()
        result = combat.run_combat()
        result_tally[result["result"]] += 1
            
    print "Results:"
    for i in range(6):
        print "{0}: {1}".format(result_table[i], result_tally[i])
    
if __name__ == "__main__":
    main()
