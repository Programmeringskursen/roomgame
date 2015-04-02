class Character(object):

    def __init__(self, name, position):
	self.content = []
	self.name = name
	self.position = position

    def pick_up(self, obj):
	"Pick up things from the room the character is in."
	if not obj in self.position.content:
	    return "THERE IS NO SUCH THING! ARE YOU HALLUCINATING?"
	self.position.content.remove(obj)
	self.content.append(obj)
	return "You picked up "+str(obj)+"."

    def drop(self, obj):
	"Drop things in the characters current room."
	if not obj in self.content:
	    return "You can not drop what you do not have."
	self.content.remove(obj)
	self.position.content.append(obj)
	return "You dropped "+str(obj)+"."



    def move(self, direction):
        if direction=="north":
            if self.position.north == False:
                return "You can't, there is no door here."
            else:
	        self.position = self.position.north
                return "You enter the "+self.position.name+"."
        elif direction=="south":
        
            if self.position.south == False:
                return "You can't, there is no door here."
            else:
                self.position = self.position.south
                return "You enter the "+self.position.name+"."
        elif direction=="west":
            
            if self.position.west == False:
                return "You can't, there is no door here."
            else:
                self.position = self.position.west
                return "You enter the "+self.position.name+"."
        elif direction=="east":

            if self.position.east == False:
                return "You can't, there is no door here."
            else:
                self.position = self.position.east
                return "You enter the "+self.position.name+"."


    def __str__(self):
        inventory = []
        for obj in self.content:
            inventory.append(str(obj))
        return "You are in "+self.position.name+". "+"In your inventory there are " + " and ".join(inventory)+"."
