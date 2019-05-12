import poke
import time
import pygame
import battle
import items
import Pokemon
import database


WIDTH = 800
HEIGHT = 400
BAG_MAX_SIZE = 20
POKEMON_MAX_SIZE = 6
SQ_SIZE = 20


def detect_keyboard(x_change, y_change):
    control_signal = None #start select save a b bar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -1
            elif event.key == pygame.K_RIGHT:
                x_change = 1
            if event.key == pygame.K_UP:
                y_change = 1
            elif event.key == pygame.K_DOWN:
                y_change = -1
            if event.key == pygame.K_s:
                control_signal = 's'
            elif event.key == pygame.K_z:
                control_signal = 'a'
            elif event.key == pygame.K_x:
                control_signal = 'b'
            elif event.key == pygame.K_SPACE:
                control_signal = 'e'

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                x_change = 0

    return x_change,y_change, control_signal

def update_position(player, x_change, y_change):
    if y_change == -1:
        player.moveDown()
    elif y_change == 1:
        player.moveUp()
    if x_change == -1:
        player.moveLeft()
    elif x_change == 1:
        player.moveRight()


def initialization():
    print("Welcome to the bifas game!")
    #see if its to start a new game or continue
    saved = None
    while saved is None:
        s = input("Start from saved game? y/n")
        if s == 'y' or s == 'n':
            saved = s

    if saved == 'y':
        while True:
            loaded_name = input("What's your name?")
            loaded_player = load_player(loaded_name)
            if loaded_player is not False:
                print("So let the adventure continue!")
                return loaded_player

    else:
        #todo change this and return the player
        name = input("What's your name?")
        gender = None
        while gender is None:
            g = input("Are you (B)oy or (G)irl?")
            if g == 'B' or g == 'G':
                gender = g

        if gender == 'B':
            char_img = 0
        else:
            char_img = 1

        n_player = poke.Player(name=name, img=char_img)
        n_player.position = [100, 100]
        print("So let the adventure begin!")
        return n_player


def create_map(player):
    mapa = []
    mapa1 = poke.Scenario(1, WIDTH, HEIGHT)
    mapa1.add_player(player)
    mapa1.fill(1, [5 * SQ_SIZE, 10 * SQ_SIZE], [5 * SQ_SIZE, 10 * SQ_SIZE])
    mapa1.fill(1, [15 * SQ_SIZE, 20 * SQ_SIZE], [5 * SQ_SIZE, 10 * SQ_SIZE])
    #mapa1.fill(2, [10 * SQ_SIZE, 11 * SQ_SIZE], [15 * SQ_SIZE, 16 * SQ_SIZE])
    #mapa1.fill(2, [30 * SQ_SIZE, 31 * SQ_SIZE], [15 * SQ_SIZE, 16 * SQ_SIZE])
    #mapa1.fill(3, [30 * SQ_SIZE, 31 * SQ_SIZE], [5 * SQ_SIZE, 6 * SQ_SIZE])

    mapa2 = poke.Scenario(2, WIDTH, HEIGHT)
    mapa2.fill(1, [25 * SQ_SIZE, 35 * SQ_SIZE], [14 * SQ_SIZE, 19 * SQ_SIZE] )

    mapa.append(mapa1)
    mapa.append(mapa2)
    return mapa

def create_all_TM():
    TMs = {}
    tm33 = items.TMs(name="Thundershock", id=33, img = 0, description="lalal",  TM_number=33, location = [5,5])
    TMs.add({tm33.TM_number: tm33})
    return TMs

def found_item(mapa):
    for item in mapa.items:
        if mapa.player.position == item.location:
            mapa.player.add_item(item)
            mapa.remove_item(item)
            return True
    return False

def found_pokemon(mapa):
    for pokemon in mapa.pokemons:
        if mapa.player.position == pokemon.location:
            #todo start battle
            mapa.remove_pokemon(pokemon)
            return True
    return False


def found_trainer(mapa):
    for trainer in mapa.trainers:
        if mapa.player.position == trainer.position:
            #todo start battle
            return True
    return False


def handle_option(control_signal):
    if control_signal == 's':
        save(player)
    elif control_signal == 'a':
        pass
    elif control_signal == 'b':
        pass
    elif control_signal == 'e':
        pass


def save(player2save):
    confirmation = None
    print("Do you want to save? (y)es/(n)o")
    while confirmation is None:
        c = input('->')
        if c == 'y' or c == 'n':
            confirmation = c
        else:
            print("Wrong input")
    if confirmation == 'y':
        print("saving...")
        save_player(player2save)
        print("game saved")

    else:
        print("so why you clicked on this dumb xD")
        time.sleep(0.5)


def load_player(name):
    db = database.Database("pokemon.db")
    player_chosen = db.take_player(name)
    bag = db.take_bag()
    party = db.take_party()
    if len(player_chosen) == 1:
        new_player = poke.Player(name=player_chosen[0][0], img=player_chosen[0][1])
        new_player.position = [player_chosen[0][2], player_chosen[0][3]]
        new_player.crachas = player_chosen[0][4]
    else:
        return False

    for each in bag:
        item = items.TMs(name=each[0], id=33, img=0, description="Prepare to get electrified", TM_number=33)
        new_player.add_item(item)

    for p in party:
        att1 = Pokemon.Attack(name=p[3], damage=40, pp=15)
        att2 = Pokemon.Attack(name=p[4], damage=40, pp=15)
        att3 = Pokemon.Attack(name=p[5], damage=40, pp=15)
        att4 = Pokemon.Attack(name=p[6], damage=40, pp=15)
        pok = Pokemon.Pokemon(name=p[0], types=[p[1], p[2]], level=p[7], nature=p[9], gender=p[8],
                               attacks=[att1, att2, att3, att4])
        pok.add_stats(sp_att=p[10], sp_def=p[11], speed=p[12], defense=[13], att=p[14], acc=p[15],
                       hp=p[16], max_hp=p[17], xp=p[18], xp2next=p[19])
        new_player.add_pokemon(pok)
    return new_player
    #todo close db?


def save_player(player2save):
    db = database.Database("pokemon.db")

    db.update_player(player2save)
    db.update_party(player2save)
    db.update_bag(player2save)


if __name__ == "__main__":

    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = initialization()

    x_change = 0
    y_change = 0
    #t1 = threading.Thread(target=detect_keyboard, args= (x_change,y_change))
    #t1.start()

    mapa = create_map(player)
    tm33 = items.TMs(name="Thundershock", id=33, img=0, description="lalal", TM_number=33, location=[13*SQ_SIZE, 14*SQ_SIZE])

    Thundershock = Pokemon.Attack(name="Thundershock", damage=40, pp =15)
    TailWhip = Pokemon.Attack(name="Tail Whip", damage=0, pp =40)
    Tackle = Pokemon.Attack(name="Tackle", damage=20, pp=40)
    pika = Pokemon.Pokemon(name="pika", types="Electric", level=5, nature="Calm", gender='M',
                              attacks=[Thundershock, TailWhip])
    eevee = Pokemon.Pokemon(name="eevee", types="Normal", level=5, nature="Calm", gender='M',
                              attacks=[Tackle, TailWhip])
    ratata = Pokemon.Pokemon(name="ratata", types="Normal", level=2, nature="Calm", gender='M',
                             attacks=[Tackle, TailWhip])

    ratata.location = [30*SQ_SIZE,15*SQ_SIZE]

    trainer1 = poke.Trainer(name="Sega", img = 0, pos=[10*SQ_SIZE, 15*SQ_SIZE], phrase="Get Ready")
    trainer1.add_pokemon(eevee)

    player.add_pokemon(pika)

    mapa[0].add_item(tm33)
    mapa[0].add_trainer(trainer1)
    mapa[0].add_pokemon(ratata)

    while True:
        x_change, y_change, control_signal = detect_keyboard(x_change, y_change)
        if control_signal is not None:
            handle_option(control_signal)

        update_position(player, x_change, y_change)
        if found_item(mapa[0]):
            print("Item founded")
            time.sleep(1)
        elif found_pokemon(mapa[0]):
            print("Pokemon appeared")
            time.sleep(1)
            b = battle.Battle()
            winner, looser = b.battle(player.party[0], ratata)
            b.give_xp(winner, looser)
            time.sleep(1)
        elif found_trainer(mapa[0]):
            print("Trainer Challenge")
            time.sleep(1)
        else:
            print(mapa[0])
            #print(p.position)
            time.sleep(0.5)
        pygame.display.update()
        clock.tick(10)
