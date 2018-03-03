from typeclasses.objects import Object
import string
import random

class TileBag(Object):
    """
    The tile bag contains the tiles for a given game, 
    starting from a standard Scrabble tile set.
    """
    def at_object_creation(self):
        """
        Called when object is first created
        """
        with open("./commands/CSW15.txt") as word_file:
            self.db.csw15 = set(word.strip().lower() for word in word_file)
        self.db.centre = ""
        self.db.bagsize = 100
        self.db.tiledict = {'A' : 9,
        'B' : 2,
        'C' : 2,
        'D' : 4,
        'E' : 12,
        'F' : 2,
        'G' : 3,
        'H' : 2,
        'I' : 9,
        'J' : 1,
        'K' : 1,
        'L' : 4,
        'M' : 2,
        'N' : 6,
        'O' : 8,
        'P' : 2,
        'Q' : 1,
        'R' : 6,
        'S' : 4,
        'T' : 6,
        'U' : 4,
        'V' : 2,
        'W' : 2,
        'X' : 1,
        'Y' : 2,
        'Z' : 1,
        '?' : 2
        }
        self.db.tilestring = list(''.join([L*self.db.tiledict[L] for L in string.ascii_uppercase+'?']))

    def reset_bag(self):
        """
        called by the reset command
        """

    def check_bag_size(self):
        """
        Called by the draw command. Returns the size of the bag at any point in time.
        """
        return len(self.db.tilestring)

    def remove_tiles(self, num):
        """
        Called by the draw command. 

        Args:
            num (integer): The number of tiles to be drawn

        Returns:
            drawntiles (list): A list of tiles drawn out

        Notes:
            This function should be called only after checking if 
            the tile bag has enough tiles using check_bag_size(self)
        """
        drawntiles = [self.db.tilestring.pop(random.randrange(len(self.db.tilestring))) for _ in xrange(num)]
        return drawntiles