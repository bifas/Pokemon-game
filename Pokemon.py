MAX_LEVEL = 100
MIN_LEVEL = 1
MAX_ATTACKS = 4


class Pokemon:
    def __init__(self, name, types , level, nature, gender, attacks):
        self.name = name
        self.types = types
        self.attack_list = attacks
        self.level = level
        self.nature = nature
        self.gender = gender

        self.sp_att = 1
        self.sp_def = 1
        self.speed = 1
        self.defense = 1
        self.att = 1
        self.acc = 1
        self.max_hp = 100
        self.hp = self.max_hp
        self.xp = 0
        self.xp2next = self.level**2 #todo see how it works on the original game

        self.location = None

    def add_stats(self, sp_att, sp_def, speed, defense, att, acc, hp, max_hp, xp, xp2next):
        self.sp_att = sp_att
        self.sp_def = sp_def
        self.speed = speed
        self.defense = defense
        self.att = att
        self.acc = acc
        self.max_hp = max_hp
        self.hp = hp
        self.xp = xp
        self.xp2next = xp2next

    def add_attack(self, attack):
        if len(self.attack_list) >= 4:
            return False
        else:
            self.attack_list.append(attack)
            return True


    def rename(self, new_name):
        if len(new_name) >1:
            self.name = new_name
            return True
        return False

    def remove_attack(self, attack):
        if attack in self.attack_list:
            if len(self.attack_list) > 1:
                self.attack_list.remove(attack)
                return True
        return False

    def restore_hp(self):
        self.hp = self.max_hp

    def nature_effects(self):
        pass


    def evolve(self):
        pass

    def is_dead(self):
        if self.hp <= 0:
            return True
        return False

    def __str__(self): #just defining this for the battle:
        line1 = "Your pokemon is: {}\n".format(self.name)
        line2 = "level:{} hp:{}\n".format(self.level,self.hp)
        line3 = "Choose one of the following: \n"
        #todo dont like this string concatenation
        line4 = ""
        for att in self.attack_list:
            line4 = line4 + att.name + "\n"
        return "{}{}{}{}".format(line1, line2, line3, line4)

#class pikachu(Pokemon):
 #   def __init__(self):

class Attack:
    def __init__(self, name, damage, pp):
        self.name = name
        self.damage = damage
        self.pp = pp

    def use_attack(self):
        if self.pp > 0:
            self.pp -= 1
            return self.damage
        else:
            return 0

    def suffer_attack(self, pokemon, attack):
        pokemon.hp -= self.damage


    def __str__(self):
        return self.name

