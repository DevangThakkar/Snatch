# -*- coding: utf-8 -*-
"""
Connection screen

Texts in this module will be shown to the user at login-time.

Evennia will look at global string variables (variables defined
at the "outermost" scope of this module and use it as the
connection screen. If there are more than one, Evennia will
randomize which one it displays.

The commands available to the user when the connection screen is shown
are defined in commands.default_cmdsets. UnloggedinCmdSet and the
screen is read and displayed by the unlogged-in "look" command.

"""

from django.conf import settings
from evennia import utils

CONNECTION_SCREEN = """
|b==============================================================|n
 Welcome to |gSNATCH|n by Devang Thakkar!

 If you have an existing account, connect to it by typing:
      |wconnect <username> <password>|n
 If you need to create an account, type (without the <>'s):
      |wcreate <username> <password>|n

Usage:
|wstart|n - create a new game with a fresh set of tiles 
|wdraw <num>|n - draw <num> number of tiles, where num is [1-7]
|wdelete|n - delete a bag from the game
|wcheck*|n - check number of tiles left in the bag
|wcheckbags*|n - check number of bags in the game

It is possible that multiple bags are created if more than one
|wstart|n commands have been issued. You may choose to keep the
bags or delete them - it doesn't really matter.

Note: Commands marked with an asterisk show output only to you.
|b==============================================================|n"""
