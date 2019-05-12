import sqlite3
import Pokemon
import poke
import items
# C:\Users\valveirinho\AppData\Local\Programs\Python\Python36

class Database:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.c = self.connection.cursor()
        try:
            self.c.execute('''CREATE TABLE Player(name text, image text, pos_x int, pos_y int, badges int)''')
        except Exception as e:
            print("Exception {}".format(e))

        try:
            self.c.execute('''CREATE TABLE Party(pokemon text, type1 text, type2 text, att1 text, att2 text, att3 text,
            att4 text, level int, gender char, nature text, sp_att int, sp_def int, speed int, defense int,
            att int, acc int, hp int, max_hp int, xp int, xp2next int)''')
        except Exception as e:
            print("Exception {}".format(e))

        try:
            self.c.execute('''CREATE TABLE Bag(item text, quantity int)''')
        except Exception as e:
            print("Exception {}".format(e))

    def new_player(self, p):
        try:
            self.c.execute("insert into Player values('{}', '{}', {}, {}, {})".format(p.name, p.img, p.position[0],
                                                                                      p.position[1], len(p.crachas)))
            self.connection.commit()
            return True
        except Exception as e:
            print("not executed, error: {}".format(e))
            return False

    def add_pokemon(self,p):
        try:
            self.c.execute("insert into Party values('{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', {},{},"
                " {}, {}, {}, {}, {}, {}, {}, {})".format(p.name, p.types[0], p.types[1], p.attack_list[0].name,
                p.attack_list[1].name, p.attack_list[2].name, p.attack_list[3].name, p.level, p.gender, p.nature,
                p.sp_att, p.sp_def, p.speed, p.defense, p.att, p.acc, p.hp, p.max_hp, p.xp, p.xp2next))
            #self.connection.commit()
            return True
        except Exception as e:
            print("not executed, error: {}".format(e))
            return False

    def add_item(self,item,qt):
        try:
            self.c.execute("INSERT INTO Bag VALUES('{}', {})".format(item.name,qt))
            #self.connection.commit()
        except Exception as e:
            print("Unable to add item {}, error: {}".format(item.name, e))

    #fetchall for retriving a list and fetchone to retrieve an iterator

    def take_player(self,name):
        #todo SQL injection prevention
        self.c.execute("SELECT * FROM Player WHERE name = '{}' ".format(name))
        #self.c.execute("SELECT * FROM Player")
        return self.c.fetchall()

    def take_party(self):
        self.c.execute("SELECT * FROM Party")
        return self.c.fetchall()

    def take_bag(self):
        self.c.execute("SELECT * FROM Bag")
        return self.c.fetchall()


    def delete_party(self):
        try:
            self.c.execute("delete from Party")
            self.connection.commit()
        except Exception as e:
            print("Delete party error: {}".format(e))

    def delete_player(self, player):
        try:
            self.c.execute("delete from Player where name = '{}'".format(player.name))
            self.connection.commit()
        except Exception as e:
            print("Delete party error: {}".format(e))

    def delete_bag(self):
        try:
            self.c.execute("delete from Bag")
            self.connection.commit()
        except Exception as e:
            print("Delete bag error: {}".format(e))

    def update_party(self, player):
        self.delete_party()
        for pokemon in player.party:
            self.add_pokemon(pokemon)
        self.connection.commit()

    def update_player(self,player):
        try:
            self.c.execute("UPDATE Player "
                           "SET  pos_x = {}, pos_y = {}, badges = {}) "
                           "WHERE name = '{}'".format(player.position[0], player.position[1], len(player.crachas),
                                                      player.name))
            self.connection.commit()
        except Exception as e:
            print("Update player error: {}".format(e))

    def update_bag(self, player):
        self.delete_bag()
        for item in player.bag:
            self.add_item(item, 1) #todo for now, because bag needs to be a dictionary with the item and the quantity
        self.connection.commit()

    def close(self):
        self.connection.close()

if __name__ == "__main__":

    db = Database("pokemon.db")


    Thundershock =  Pokemon.Attack(name="Thundershock", damage=40, pp=15)
    pika = Pokemon.Pokemon(name="pikachu", types=["Electric", "Electric"], level=5, nature="Calm", gender='M',
                           attacks=[Thundershock, Thundershock, Thundershock, Thundershock])
    #db.add_pokemon(pika)
    #db.restart_party()

    # player1 = poke.Player(name="zeca", img=0)
    # player2 = poke.Player(name="sega", img=0)
    # player3 = poke.Player(name="name12", img=0)
    # tm33 = items.TMs(name="Thundershock", id=33, img=0, description="lalal", TM_number=33)
    # player1.add_item(tm33)
    # player1.add_item(tm33)
    # player1.add_pokemon(pika)
    # player1.add_pokemon(pika)
    #
    # db.delete_player(player1)
    # db.new_player(player1)
    # db.update_party(player1)
    # db.update_bag(player1)
    # db.new_player(player2)
    # a = db.delete_player(player3)
    # b = db.delete_player(player1)
    player = db.take_player("teste123")
    bag = db.take_bag()
    party = db.take_party()

    if len(player) == 1:
        new_player = poke.Player(name=player[0][0],img=player[0][1])
        new_player.position = [player[0][2], player[0][3]]
        new_player.crachas = player[0][4]
    for each in bag:
        item = items.TMs(name=each[0], id=33, img=0, description="Prepare to get electrified", TM_number=33)
        new_player.add_item(item)
    for p in party:
        att1 = Pokemon.Attack(name=p[3], damage=40, pp=15)
        att2 = Pokemon.Attack(name=p[4], damage=40, pp=15)
        att3 = Pokemon.Attack(name=p[5], damage=40, pp=15)
        att4 = Pokemon.Attack(name=p[6], damage=40, pp=15)
        poke = Pokemon.Pokemon(name=p[0], types=[p[1], p[2]], level=p[7], nature=p[9], gender=p[8],
                               attacks=[att1, att2, att3, att4])
        poke.add_stats(sp_att=p[10], sp_def=p[11], speed=p[12], defense=[13], att=p[14], acc=p[15],
                       hp=p[16], max_hp=p[17], xp=p[18], xp2next=p[19])
        new_player.add_pokemon(poke)

    # print(new_player)
    # for poke in new_player.party:
    #     print(poke)
    # print(new_player.bag)