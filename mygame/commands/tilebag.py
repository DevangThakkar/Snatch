import time
import typeclasses
from evennia import create_object
from evennia import Command as BaseCommand
from typeclasses.tilebag import TileBag
from evennia.utils import search
from evennia import Command
from evennia import DefaultObject
from typeclasses.accounts import Account

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
        for acc in Account.objects.all():
            acc.msg("New bag created by "+self.caller.key+"!")
            # acc.msg("Bag size: "+str(bag.check_bag_size()))
            # acc.msg(bag.db.tilestring)
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
        bag_obj = search.objects('bag1')
        if not bag_obj:
            self.caller.msg("(Only you can see this)")
            self.caller.msg("No tile bags exist. Create a bag using <start>")
        else:
            self.caller.msg("(Only you can see this)")
            self.caller.msg("Number of tiles left is: "+str(bag_obj[0].check_bag_size()))

class CmdCheckBags(Command):
    """
    Check number of bags

    Usage:
        checkbags

    Checks the number of tile bags in the room. Ideally there should 
    only be one bag in the room
    """
    key = "checkbags"
    lock = "cmd:all()"
    aliases = ["<checkbags>", "checkbag", "<checkbag>"]
    help_category = "General"

    def func(self):
        "implements the actual functionality"
        bag_obj = search.objects('bag1')
        if not bag_obj:
            self.caller.msg("(Only you can see this)")
            self.caller.msg("No tile bags exist. Create a bag using <start>")
        else:
            self.caller.msg("(Only you can see this)")
            self.caller.msg("Number of bags is: "+str(len(bag_obj)))

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
            self.caller.msg("(Only you can see this)")
            self.caller.msg("No tile bags exist. Create a bag using <start>")
        else:
            bag_obj[len(bag_obj)-1].delete()
            for acc in Account.objects.all():
                acc.msg("A tile bag was just killed because of "+self.caller.key+"'s whims.")
                acc.msg("Number of bags left: "+str(len(bag_obj)-1))


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
            self.caller.msg("(Only you can see this)")
            self.caller.msg("No tile bags exist. Create a bag using <start>")
        else:
            bag = bag_obj[0]
            num = self.args.strip()
            valid0 = len(num)
            if valid0 == 0:
                self.caller.msg("(Only you can see this)")
                self.caller.msg("Enter the number of tiles to be drawn along with the command")
                return
            valid1 = num.isdigit()
            if not valid1:
                self.caller.msg("(Only you can see this)")
                self.caller.msg("Enter a valid integer")
                return
            valid2 = int(num) <= 7 and int(num) >= 1
            if bag.check_bag_size() == 0:
                for acc in Account.objects.all():
                    acc.msg("Game over. The tile bag is now empty. Create a new bag using <start>")
                bag.delete()
                return
            if not valid2:
                self.caller.msg("(Only you can see this)")
                self.caller.msg("Enter a valid integer in the range [1,7]")
                return
            valid3 = int(num) <= bag.check_bag_size()
            if not valid3:
                self.caller.msg("(Only you can see this)")
                self.msg("Not enough tiles left, number of tiles left is: "+str(bag.check_bag_size()))
                return
            removed = ' '.join(bag.remove_tiles(int(num)))
            bag.db.centre = str(bag.db.centre) + " " + removed # DB Centre reminds me of Nishit
            for acc in Account.objects.all():
                acc.msg("Tile(s) removed by "+self.caller.key+" are: " + removed)
                # acc.msg(str(bag.check_bag_size())+" tiles left")
                acc.msg("Tile(s) in the centre are: " + bag.db.centre)
            
class make(Command):
    """
    Make words

    Usage:
        make <word>

    The user can choose letters from the Centre and make a word if 
    it is allowed by CSW15. The letters are then removed and added
    to the person's collection.
    """
    key = "make"
    aliases = ["<make>"]
    lock = "cmd:all()"
    help_category = "General"

    def func(self, word):
        "implements the actual functionality"
        if word.lower() not in search.objects('bag1')[0].db.csw15:
            for acc in Account.objects.all():
                acc.msg(self.caller.key + " attempted "+ word.upper() + " - which is not a word.")
        else:
            for acc in Account.objects.all():
                acc.msg(self.caller.key + " made "+ word.upper() + "!")