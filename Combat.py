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
    CRAFT_APPROACH_RATE = 0.5 # 0.5km/gs
    CRAFT_FALLBACK_RATE = 0.5 # 0.5km/gs
    STANDOFF_DISTANCE = 70.0

    def __init__(self, ufo="small scout", craft_init=["interceptor"],
                 craft_weps=[["cannon", "cannon"]], craft_mode=["aggressive"],
                 dif="beginner"):
        """Instantiate an Air Combat Simulation object.

        Keyword arguments
        ufo -- ufo type
        craft_init -- list of interceptors
        craft_weps -- list of list of interceptors' weapons
        craft_mode -- list of interceptor's attack modes
        dif -- game difficulty setting
        """
        self.difficulty = dif
        self.ufo = acsm.UFO_OPTIONS[ufo](self.difficulty)
        self.interceptor_list = []
        for i, craft in enumerate(craft_init):
            self.interceptor_list.append( \
            acsm.XC_CRAFT_OPTIONS[craft](craft_weps[i], craft_mode[i]))

        # Adjust UFO weapon cooldowns
        self.ufo.adjust_cooldown(2 * acsm.DIFFICULTY_OPTIONS[self.difficulty])

        # Initialize some variables
        self.crashpoint = .5*self.ufo.max_armor

    def initialize(self):
        """Reset the craft for another Combat."""
        self.ufo.reset()
        for craft in self.interceptor_list:
            craft.reset()
            craft.distance_to_target = AirCombatSimulation.STANDOFF_DISTANCE

    def run_combat(self):
        """Run a single combat.

        Return the end state of the combat.
        """
        self.initialize()
        projectile_list = list()
        clock = 0
        interceptors_alive = True

        # Simulation runs until one of the following situations occurs:
        # UFO crashed/destroyed.
        # There are no interceptors alive or projectiles in the air.
        while ((interceptors_alive or projectile_list != []) and
               self.ufo.current_armor > self.crashpoint):

#            print "time: {0}".format(clock)
#            for craft in self.interceptor_list:
#                print "interceptor armor: {0}/(1)".format(craft.current_armor,
#                                                          craft.max_armor)
#            print "ufo armor: {0}/{1}".format(self.ufo.current_armor,
#                                              self.ufo.max_armor)
#            for missile in projectile_list:
#                print "missile in flight: {0}, {1}km from target".format(\
#                    missile.weapon.projectile_name, missile.distance)


            # Iterate clock
            clock += 1
            if clock > 10000:
                sys.exit("Maximum allowable time exceeded.  Quitting...")

            # Let missiles fly
            for proj in projectile_list[:]:
                if proj.fly():
#                    print "Chance to hit: {0}".format((proj.weapon.accuracy * \
#                        proj.target.dodge_multiplier))
                    if random.random() < proj.weapon.accuracy * \
                        proj.target.dodge_multiplier:
                        if proj.target == self.ufo:
                            # Deals 50%-100% damage
                            boom = int(round((1+random.random())/2 *
                                             proj.weapon.damage))
                        else:
                            # Deals 0%-100% damage
                            boom = int(round(random.random() *
                                             proj.weapon.damage))
                        proj.target.take_damage(boom)
#                        print "The {0} hits the {1} for {2} damage.".format(\
#                            proj.weapon.projectile_name, proj.target.name, boom)
#                    else:
#                        print "The {0} misses the {1}.".format(\
#                            proj.weapon.projectile_name, proj.target.name)
                    projectile_list.remove(proj)

            interceptors_alive = False
            for craft in self.interceptor_list:
                # Interceptor retreats if it has no ammo.
                # Otherwise it advances up to its ideal range.
                has_ammo = False
                for wep in craft.weapons:
                    if wep.current_ammo > 0:
                        has_ammo = True
                if has_ammo:
                    if craft.distance_to_target > craft.preferred_distance:
                        craft.distance_to_target -= \
                            AirCombatSimulation.CRAFT_APPROACH_RATE
                else:
                    craft.distance_to_target += \
                        AirCombatSimulation.CRAFT_FALLBACK_RATE
                # If no interceptors are still alive, combat may end.
                # Retreating behind standoff distance counts as being "dead".
                if (craft.current_armor > 0 and
                    craft.distance_to_target <=
                    AirCombatSimulation.STANDOFF_DISTANCE):
                    interceptors_alive = True

            # Tick weapons
            self.ufo.tick()
            for craft in self.interceptor_list:
                craft.tick()

            # Fire UFO Weapons
            # UFO chooses an in-range target at random.
            targetlist = []
            if self.ufo.weapons[0].is_ready_to_fire(0):
                for craft in self.interceptor_list:
                    if (craft.distance_to_target <=
                        self.ufo.preferred_distance and
                        craft.current_armor > 0):
                        targetlist.append(craft)
                if targetlist != []:
                    target = targetlist[random.randint(0, len(targetlist))-1]
                    projectile_list.append(\
                        self.ufo.weapons[0].fire(target,
                                                 target.distance_to_target))

            # Fire Interceptor Weapons
            for craft in self.interceptor_list:
                if craft.current_armor > 0:
                    for wep in craft.weapons:
                        if wep.is_ready_to_fire(craft.distance_to_target):
                            projectile_list.append(wep.fire(self.ufo,\
                                craft.distance_to_target))

        # Determine final state of simulation and return value.
        # result[0] = # interceptors destroyed
        # result[1] = # interceptors out of ammo
        # result[2] = # ufos destroyed
        # result[3] = # ufos crashed
        # result[4] = # ufos escaped

        final_state = (0, 0, 0, 0, 0)
        for craft in self.interceptor_list:
            if craft.current_armor <= 0:
                final_state = [x + y for x, y in
                               zip(final_state, (1, 0, 0, 0, 0))]
        for craft in self.interceptor_list:
            for wep in craft.weapons:
                if wep.current_ammo == 0:
                    final_state = [x + y for x, y in
                                   zip(final_state, (0, 1, 0, 0, 0))]
        if self.ufo.current_armor <= 0:
            final_state = [x + y for x, y in zip(final_state, (0, 0, 1, 0, 0))]
        elif self.ufo.current_armor <= self.crashpoint:
            final_state = [x + y for x, y in zip(final_state, (0, 0, 0, 1, 0))]
        else:
            final_state = [x + y for x, y in zip(final_state, (0, 0, 0, 0, 1))]

#        print final_state

        return {"result" : final_state}

class main(object):
    """Run on execution of Combat.py."""
    result_table = ["interceptors destroyed",
                    "interceptors out of ammo",
                    "ufos destroyed",
                    "ufos crashed",
                    "ufos escaped"]
    result_tally = [0, 0, 0, 0, 0]

###############################################################################

    print ""
    print "Select a UFO type:"
    for i in acsm.UFO_OPTIONS:
        print i
    ufo_type = raw_input("UFO type: ")
    while ufo_type not in acsm.UFO_OPTIONS:
        print "Not a valid selection."
        ufo_type = raw_input("UFO type: ")

    print ""
    print "Select an interceptor type:"
    for i in acsm.XC_CRAFT_OPTIONS:
        print i
    interceptor_type = raw_input("Interceptor type: ")
    while interceptor_type not in acsm.XC_CRAFT_OPTIONS:
        print "Not a valid selection."
        interceptor_type = raw_input("Interceptor type: ")
    interceptor_list = [interceptor_type]
    
    print ""
    print "Select two weapon types:"
    for i in acsm.WEAPON_OPTIONS:
        print i
    weapon_selection1 = raw_input("1st Weapon type: ")
    while weapon_selection1 not in acsm.WEAPON_OPTIONS:
        print "Not a valid selection."
        weapon_selection1 = raw_input("1st Weapon type: ")
    weapon_selection2 = raw_input("2nd Weapon type: ")
    while weapon_selection2 not in acsm.WEAPON_OPTIONS:
        print "Not a valid selection."
        weapon_selection2 = raw_input("2nd Weapon type: ")
    weapon_list = [[weapon_selection1, weapon_selection2]]

    print ""
    print "Set the interceptor's attack mode:"
    for i in acsm.ATTACK_MODE_OPTIONS:
        print i
    mode_selection = raw_input("Attack mode: ")
    while mode_selection not in acsm.ATTACK_MODE_OPTIONS:
        print "Not a valid selection."
        mode_selection = raw_input("Attack mode: ")
    mode_list = [mode_selection]        

    print ""
    number_of_interceptors = int(raw_input(\
        "How many copies of this interceptor would you like? (min 1) "))

    print ""
    print "Select a difficulty mode:"
    for i in acsm.DIFFICULTY_OPTIONS:
        print i
    difficulty_mode = raw_input("Difficulty mode: ")
    while difficulty_mode not in acsm.DIFFICULTY_OPTIONS:
        print "Not a valid selection."
        difficulty_mode = raw_input("Difficulty mode: ")
        
    print""
    number_of_rounds = int(raw_input(\
        "How many rounds of combat do you want to simulate? (min 1) "))  

###############################################################################

# Uncomment and edit this section to run more complex simulations.
# Note that interceptor_list, weapon_list, and mode_lists are lists, and
# weapon_list is actually a LIST OF LISTS.

#    ufo_type = "battleship"
#    interceptor_list = ["avenger"]
#    weapon_list = [["cannon", "cannon"]]
#    mode_list = ["standard"]
#    number_of_interceptors = 4    
    
    # Uncomment for lazy multiplying of interceptor count
    for i in range(number_of_interceptors - 1):
        interceptor_list.append(interceptor_list[0])
        weapon_list.append(weapon_list[0])
        mode_list.append(mode_list[0])

#    number_of_rounds = 1000

###############################################################################

#    print "List of interceptors:"
#    for i in range(len(interceptor_list)):
#        print zip(interceptor_list, weapon_list, mode_list)[i]

    combat = AirCombatSimulation(ufo=ufo_type,
                                 craft_init=interceptor_list,
                                 craft_weps=weapon_list,
                                 craft_mode=mode_list,
                                 dif=difficulty_mode)

    number_of_interceptors = len(interceptor_list)

    for i in range(number_of_rounds):
        combat.initialize()
        result = combat.run_combat()
        result_tally = [x + y for x, y in zip(result_tally, result["result"])]

    for i in range(len(result_tally)):
        result_tally[i] *= 100.0 / number_of_rounds

    result_tally[0] /= number_of_interceptors
    result_tally[1] /= number_of_interceptors
    result_tally[2] /= number_of_interceptors

    print "Results:"
    print "{0} combats were fought.".format(number_of_rounds)
    print "{0} interceptor(s) fought a {1} for each combat.".format(\
        len(interceptor_list), ufo_type)
    print "{0:4.1f}% of interceptors are destroyed.".format(result_tally[0])
    print "{0:4.1f}% of interceptors return to base.".format(100-result_tally[0])
    print "{0:4.1f}% of interceptors run out of ammo.".format(result_tally[1])
    print "{0:4.1f}% of ufos are destroyed.".format(result_tally[2])
    print "{0:4.1f}% of ufos crash land.".format(result_tally[3])
    print "{0:4.1f}% of ufos escape.".format(result_tally[4])

if __name__ == "__main__":
    main()
