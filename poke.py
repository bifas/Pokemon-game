import items

WIDTH = 800
HEIGHT = 400
BAG_MAX_SIZE = 20
POKEMON_MAX_SIZE = 6
SQ_SIZE = 20

class Person:

    def __init__(self, name=None, pos=None, img=None):
        self.name = name
        if pos is None:
            self.position = [0, 0]
        else:
            self.position = pos
        self.img = img

    def change_name(self, name):
        if len(name) >= 3:
            self.name = name
            return True
        else:
            return False

    def add_img(self,img): #add some logic if img does not exist
        self.img = img
        return True

    def moveUp(self):
        if self.position[1] >  0:
            self.position[1] -= SQ_SIZE
        else:
            self.position[1] = 0
        return self.position

    def moveDown(self):
        if self.position[1] < HEIGHT:
            self.position[1] += SQ_SIZE
        else:
            self.position[1] = HEIGHT
        return self.position

    def moveRight(self):
        if self.position[0] < WIDTH:
            self.position[0] += SQ_SIZE
        else:
            self.position[0] = WIDTH
        return self.position

    def moveLeft(self):
        if self.position[0] > 0:
            self.position[0] -= SQ_SIZE
        else:
            self.position[0] = 0
        return self.position


class Scenario: #todo use constants to define the terrain
    def __init__(self, id, w, h):
        if w < 1 or h < 1:
            return None
        self.id = id
        self.width = w
        self.height = h
        self.m = []
        self.player = None
        self.items = []
        self.pokemons = []
        self.trainers = []

        for x in range(self.height): #matrix initialization, maybe to heavy?
            col = []
            for y in range(self.width):
                col.append(0)
            self.m.append(col)

    def fill(self, number, range_x, range_y):
        if number > 6: #todo define better this thres (looks like magic)
            return False
        if range_x[0] > 0 and range_y[0] > 0 and range_x[1] < self.width and range_y[1] < self.height:
            for x in range(range_x[0],range_x[1]):
                for y in range(range_y[0], range_y[1]):
                    self.m[y][x] = number

            return True
        return False

    def add_player(self, player):
        self.player = player

    def add_item(self, item):
        if item.location is not None:
            if item.location[0] < self.width and item.location[1] < self.height:
                self.items.append(item)
                self.fill(3, [item.location[0], item.location[0]+1], [item.location[1], item.location[1]+1])
                return True
        return False

    def remove_item(self, item):
        self.items.remove(item)
        self.fill(0, [item.location[0], item.location[0] + 1], [item.location[1], item.location[1] + 1])

    def add_pokemon(self, pokemon):
        if pokemon.location is not None:
            if pokemon.location[0] < self.width and pokemon.location[1] < self.height:
                self.pokemons.append(pokemon)
                self.fill(2, [pokemon.location[0], pokemon.location[0]+1], [pokemon.location[1], pokemon.location[1]+1])
                return True
        return False

    def remove_pokemon(self, pokemon):
        self.pokemons.remove(pokemon)
        self.fill(0, [pokemon.location[0], pokemon.location[0] + 1], [pokemon.location[1], pokemon.location[1] + 1])


    def add_trainer(self, trainer):
        if trainer.position is not None:
            if trainer.position[0] < self.width and trainer.position[1] < self.height:
                self.trainers.append(trainer)
                self.fill(4, [trainer.position[0], trainer.position[0]+1], [trainer.position[1], trainer.position[1]+1])
                return True
        return False

    def __str__(self):
        line = ""
        for i in range(0, self.height+1,SQ_SIZE):
            line = line + "X"
            if i == 0 or i == self.height: #print the boundaries
                for j in range(0, self.width, SQ_SIZE):
                    line = line + "X"
            else:
                for j in range(0, self.width, SQ_SIZE):
                    if self.player.position == [j,i]:
                        line = line + "O"
                    elif self.m[i][j] == 0:
                        line = line + " "
                    elif self.m[i][j] == 1: #house
                        line = line + "X"
                    elif self.m[i][j] == 2: #pokemon
                        line = line + "P"
                    elif self.m[i][j] == 3: #Item
                        line = line + "I"
                    elif self.m[i][j] == 4: #Trainer
                        line = line + "T"
                    else:
                        line = line + "X"

            line = line + "X\n"

        return line

class Map:
    def __init__(self, number):
        if number < 1:
            return None
        self.nodes = set(i for i in range(number))
        self.connections = []

    def add_node(self, id):
        if id not in self.nodes:
            self.nodes.add(id)
            return True
        else:
            return False

    def add_link(self, link):
        if type(link) is list:
            for t in link:
                if type(t) is tuple:
                    if t[0] in self.nodes and t[1] in self.nodes:
                        self.connections.append(t)
                    else:
                        return  #todo here is not better to raise exception???
                else:
                    return False
            return True
        return False

class Player(Person):

    def __init__(self, name, img):
        Person.__init__(self, name = name, img=img ,pos=[0,0])
        self.bag = []
        self.party = []
        self.crachas = []

    def add_item(self, item):
        if len(self.bag) < BAG_MAX_SIZE:
            self.bag.append(item)
            return True
        else:
            return False
    def take_item(self,item):
        if item in self.bag:
            self.bag.remove(item)
            return True
        else:
            return False

    def add_pokemon(self,pokemon):
        if len(self.party) < 6:
            self.party.append(pokemon)
            return True
        else:
            return False

    def take_pokemon(self,pokemon):
        if pokemon in self.party:
            self.party.remove(pokemon)
            return True
        else:
            return False

    def swap_pokemon(self,id1,id2):
        if id1 < len(self.party) and id2 < len(self.party):
            self.party[id1], self.party[id2] = self.party[id1], self.party[id2]
            return True
        return False

    def add_cracha(self,cracha):
        self.crachas.append(cracha)
        return True

    def __str__(self):
        return "Your character is {} and you have {} pokemons".format(self.name, len(self.party))


class Trainer(Person):
    def __init__(self, name, img, pos, phrase):
        Person.__init__(self, name=name, img=img, pos=pos)
        self.party = []
        self.phrase = phrase

    def add_pokemon(self,pokemon):
        if len(self.party) < 6:
            self.party.append(pokemon)
            return True
        else:
            return False

    def __str__(self):
        return "{} is challenging you with {} pokemons: \n {}".format(self.name, len(self.party), self.phrase)
