class Bagdes:
    def __init__(self,order,img):
        self.order = order
        self.img = img

class Items:
    #items can have different purposes
    def __init__(self,name, id, img, description, location = None):
        self.name = name
        self.id = id
        self.img = img
        self.description = description
        self.location = location

    def set_location(self, location):
        self.location = location

class TMs(Items):
    def __init__(self,name, id, img, description,  TM_number, location = None):
        super().__init__(name, id, img, description, location)
        self.tm_number = TM_number


class Potions(Items):
    def __init__(self,name, id, img, description, effect, location = None ):
        super().__init__(name, id, img, description, location)
        self.effect = effect

class Berries(Items):
    def __init__(self,name, id, img, description, growth_time):
        super().__init__(name, id, img, description)
        self.growth_time = growth_time
        self.stage = "seed"
    def plant(self):
        pass

    def grow(self):
        pass

    def collect(self):
        pass

class KeyItems(Items):
    def __init__(self, name, id, img, description, location = None):
        super().__init__(name, id, img, description, location)
        #todo complete

class PokeItems(Items):
    pass

class Pokeballs(Items):
    pass
    #base catch rate

