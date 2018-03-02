import time
import typeclasses
from evennia import create_object
from evennia import Command as BaseCommand
from typeclasses.tilebag import TileBag
from evennia.utils import search
from evennia import Command
from evennia import DefaultObject

class CmdStart(Command):
    """
    Start the game

    Usage:
        start

    Starts the game with a full set of tiles
    """
    key = "start"
    lock = "cmd:all()"
    aliases = ["create", "new", "<start>", "<create>", "<new>"]
    help_category = "General"

    def func(self):
        "implements the actual functionality"
        bag = create_object("typeclasses.tilebag.TileBag", key="bag1")
        self.msg("New bag created!")
        self.msg("Bag size: "+str(bag.check_bag_size()))
        self.msg(bag)
        self.msg(bag.db.tilestring)
        return bag

class CmdCheck(Command):
    """
    Check number of tiles

    Usage:
        check

    Checks and returns the number of tiles present in the tile bag
    """
    key = "check"
    lock = "cmd:all()"
    aliases = ["size", "<check>", "<size>"]
    help_category = "General"

    def func(self):
        "implements the actual functionality"

class CmdDelete(Command):
    """
    Deletes tile bags

    Usage:
        delete

    Removes a tile bag from the system (not sure about the order)
    """
    key = "delete"
    aliases = ["remove", "<delete>", "<remove>"]
    lock = "cmd.all()"
    help_category = "General"

    def func(self):
        "implements the actual functionality"
        bag_obj = search.objects('bag1')
        if not bag_obj:
            self.caller.msg("No tile bags exist. Create a bag using <start>")
        else:
            bag_obj[len(bag_obj)-1].delete()
            self.caller.msg("A tile bag was just killed because of your whims.")
            self.caller.msg("Number of bags left: "+str(len(bag_obj)-1))


class CmdDraw(Command):
    """
    Draw tiles

    Usage:
        draw <arg>

    Draws <arg> number of tiles from the bag. Returns an error message if 
    number of tiles in the bag is less than <arg>, or if <arg> is not in 
    the range [1,7]
    """
    key = "draw"
    aliases = ["<draw>"]
    lock = "cmd:all()"
    help_category = "General"

    def func(self):
        "implements the actual functionality"
        bag_obj = search.objects('bag1')
        if not bag_obj:
            self.caller.msg("No tile bags exist. Create a bag using <start>")
        else:
            bag = bag_obj[0]
            num = self.args.strip()
            valid0 = len(num)
            if valid0 == 0:
                self.caller.msg("Enter the number of tiles to be drawn along with the command")
                return
            valid1 = num.isdigit()
            if not valid1:
                self.caller.msg("Enter a valid integer")
                return
            valid2 = int(num) <= 7 and int(num) >= 1
            if bag.check_bag_size() == 0:
                self.msg("Game over. The tile bag is now empty. Create a new bag using <start>")
            if not valid2:
                self.caller.msg("Enter a valid integer in the range [1,7]")
                return
            valid3 = int(num) <= bag.check_bag_size()
            if not valid3:
                self.msg("Not enough tiles left, number of tiles left is :"+str(bag.check_bag_size()))
                return
            self.msg("Tiles removed are: " + ' '.join(bag.remove_tiles(int(num))))
            self.msg(str(bag.check_bag_size())+" tiles left")

class CmdReset(Command):
    """
    Reset tile bag

    Usage:
        reset

    Resets the tiles in the tile bag to the initial default set
    """
    key = "reset"
    aliases = ["restart", "<reset>", "<restart>"]
    lock = "cmd:all()"
    help_category = "General"

    def func(self):
        "implements the actual functionality"
        self.msg("inside reset command")
        pass