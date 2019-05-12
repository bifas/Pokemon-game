class Battle:
    def __init__(self):
        pass
    def select_att(self,poke1, poke2):
        while True:
            choice = input("->")
            for att in poke1.attack_list:
                if att.name == choice:
                    print("{} is going to use {}".format(poke1.name, att.name))
                    poke2.hp -= att.damage
                    return
            print("your attack does not exist, try again!")

    def win_battle(self,poke1, poke2):
        if poke2.is_dead():
            print("{} WON!".format(poke1.name))
            return True

    def battle(self, poke1, poke2):
        while True:
            print(poke1)
            print(poke2)
            self.select_att(poke1, poke2)
            if self.win_battle(poke1, poke2):
                return poke1, poke2
            self.select_att(poke2, poke1)
            if self.win_battle(poke2, poke1):
                return poke2, poke1

    # the idea is to have a fight with several pokemons, like a trainers battle
    def trainer_encounter(self,player1, player2):
        pass

    def give_xp(self,winner, looser):
        xp = 2.5 * (looser.level ** 1.5)
        print("{} won {} xp".format(winner.name, xp))
        winner.xp += xp
        if winner.xp > winner.xp2next:
            winner.level += 1
            print("{} is now in level {}".format(winner.name, winner.level))
        winner.xp2next = winner.xp2next * 2
        # doubles, but the actual xp is not reseted (as in pokemon, what is displayed is different
