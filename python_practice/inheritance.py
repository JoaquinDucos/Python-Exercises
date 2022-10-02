#Inheritance : create a class (Child) based on another class (Parent)
class Player:

    def __init__(self, pnombre, apellido):
      self.pnombre = pnombre
      self.apellido = apellido

class NewPlayer(Player):

     def __init__(self, pnombre, apellido, total):

        Player.__init__(self, pnombre, apellido)
        self.total = total

     def getDetails(self):
        return "%s %s has spent %s in total" % (self.pnombre, self.apellido, self.total)

newP = NewPlayer("Juan", "Marchisio", "1000")

print(newP.getDetails())