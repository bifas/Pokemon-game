import poke
import Pokemon
import battle
WIDTH = 800
HEIGHT = 400
SQ_SIZE = 20


if __name__ == "__main__":
    # # each "square is 20*20"
    # player = poke.Player(name='bifas', img=0)
    # player.position = [100,100]
    # mapa = poke.Scenario(1,WIDTH,HEIGHT)
    # mapa.add_player(player)
    # mapa.fill(1, [5*SQ_SIZE, 10*SQ_SIZE], [5*SQ_SIZE,10 *SQ_SIZE])
    # mapa.fill(1, [15*SQ_SIZE, 20*SQ_SIZE], [5*SQ_SIZE, 10*SQ_SIZE])
    # mapa.fill(2, [10 * SQ_SIZE, 11 * SQ_SIZE], [15 * SQ_SIZE, 16  * SQ_SIZE])
    # mapa.fill(2, [30 * SQ_SIZE, 31 * SQ_SIZE], [15 * SQ_SIZE, 16 * SQ_SIZE])
    # mapa.fill(3, [30 * SQ_SIZE, 31 * SQ_SIZE], [5 * SQ_SIZE, 6 * SQ_SIZE])
    # print(mapa)
    # player.moveLeft()
    # print(mapa)
    # player.moveUp()
    # print(mapa)
    Thundershock = Pokemon.Attack(name="Thundershock", damage=40, pp =15)
    TailWhip = Pokemon.Attack(name="Tail Whip", damage=0, pp =40)
    Tackle = Pokemon.Attack(name="Tackle",damage=20, pp = 40)
    pika = Pokemon.Pokemon(name= "pika", types= "Electric", level = 5, nature= "Calm", gender= 'M',
                              attacks= [Thundershock, TailWhip])
    eevee = Pokemon.Pokemon(name= "eevee", types="Normal", level = 5, nature= "Calm", gender= 'M',
                              attacks= [Tackle, TailWhip])
    b = battle.Battle()
    winner, looser = b.battle(pika, eevee)
    b.give_xp(winner, looser)


