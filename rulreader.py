# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 17:20:38 2014

@author: adam
"""

import os
import glob
import acs_module as acsm

class RulReader(object):
    """This class can read .rul files and return information."""

    DEFAULT_PATH = '/home/adam/Games/OpenXcom/bin/data/Ruleset'

    def __init__(self, path=DEFAULT_PATH):
        """Search path for .rul files and generate a list of them for parsing.

        Keyword arguments
        path -- .rul file directory
        """
        self.file_list = []
        self.weapon_list = []
        self.ufo_list = []
        self.interceptor_list = []

        for filename in glob.glob(os.path.join(path, '*.rul')):
            self.file_list.append(filename)

    def get_weapons(self):
        """Searches through all .rul files in the RulReader's path.

        Returns a dictionary of Weapon objects.
        """
        self.weapon_list = []
        for filename in self.file_list:
            open_file = open(filename)
            while True:
                current_line = open_file.readline()
                if current_line == "":
                    # Reached end of file.  Move on.
                    break
                if "craftWeapons" in current_line:
                    # Make the Weapons and add them to weapon_list.
                    # Then break.
                    break

    def get_xc_craft(self):
        """Searches through all .rul files in the RulReader's path.

        Returns a list of Craft objects for XCOM interceptors.
        """
        pass

    def get_ufo_craft(self):
        """Searches through all .rul files in the RulReader's path.

        Returns a list of Craft objects for UFOs.
        """
        pass
