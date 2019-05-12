import unittest
import poke
import items


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.img_boy = "boy.png"
        self.img_girl = "girl.png"
        self.name = 'test'
        self.position = [0,0]
        self.personage = poke.Person(self.name, self.position, self.img_boy)
        #  self.phrase = "Get prepared!" this one goes on specific

    def tearDown(self):
        pass

    def test_person_init(self):
        self.assertIsNotNone(poke.Person(self.name, self.position, self.img_girl))

    def test_change_name(self):
        self.assertTrue((self.personage.change_name('Nato')))
        self.assertFalse((self.personage.change_name('')))
        self.assertFalse((self.personage.change_name(' ')))

    def test_boy_or_girl(self):
        self.assertTrue((self.personage.add_img(self.img_boy)))
        self.assertTrue((self.personage.add_img(self.img_girl)))
        #self.assertFalse((self.personage.add_img(None)))



class TestScenario(unittest.TestCase): #matrix with information about the terrain

    def setUp(self):
        self.WIDTH = 100
        self.HEIGHT = 80
        self.fillx = [10,20]
        self.filly = [10,20]
        self.identifier = 0
        self.scenario = poke.Scenario(1, self.WIDTH,self.HEIGHT)
        self.item1 = items.TMs(name="Thundershock", id=33, img = 0, description="lalal",  TM_number=33, location = [5,5])
        self.item2 = items.TMs(name="Thunder", id=50, img=0, description="lalal", TM_number=50, location=[5000, 5])

    def tearDown(self):
        pass

    def test_create(self): #todo left to test the unique id (maybe map has the list an assigns one)
        self.assertIsNotNone(poke.Scenario(1, self.WIDTH,self.HEIGHT))
        #self.assertIsNone(poke.Scenario(2, -1, self.HEIGHT))



    def test_fill(self):
        self.assertTrue(self.scenario.fill(0, self.fillx, self.filly))
        self.assertTrue(self.scenario.fill(1,self.fillx, self.filly)) # fill with 1 the values of the matrix
        self.assertTrue(self.scenario.fill(2, self.fillx, self.filly))
        self.assertTrue(self.scenario.fill(3, self.fillx, self.filly))
        self.assertTrue(self.scenario.fill(4, self.fillx, self.filly))
        self.assertTrue(self.scenario.fill(5, self.fillx, self.filly))
        self.assertTrue(self.scenario.fill(6, self.fillx, self.filly))
        self.assertFalse(self.scenario.fill(7, self.fillx, self.filly)) # filling only until numver 6
        self.assertFalse(self.scenario.fill(1, [-1, 10], self.filly))
        self.assertFalse(self.scenario.fill(1, [10, 20], [-1, 10]))
        self.assertFalse(self.scenario.fill(1, [99, 101], self.filly))
        self.assertFalse(self.scenario.fill(1, self.fillx, [79, 81]))
        self.assertFalse(self.scenario.fill(1, [99, 101], [79, 81]))

    def test_add_item(self):
        self.assertTrue(self.scenario.add_item(self.item1))
        self.assertFalse(self.scenario.add_item(self.item2))


class TestMap(unittest.TestCase): #connections between scenarios

    def setUp(self):
        self.numb = 5
        #self.nodes = set(i for i in range(self.numb)) do this in the implementation
        self.connections = [(0, 1), (1, 2)]
        self.maps = poke.Map(5)

    def tearDown(self):
        pass

    def test_create(self):
        self.assertIsNotNone(poke.Map(self.numb))
        # self.assertIsNone(poke.Map(-1))

    def test_add_link(self):
        self.assertTrue(self.maps.add_link(self.connections))
        self.assertFalse(self.maps.add_link([(-1, 0)]))

    def test_add_node(self):
        self.assertTrue(self.maps.add_node(5)) #add a new node
        self.assertFalse(self.maps.add_node(1)) #add an already existing node


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.main_img = 0
        self.p = poke.Player("bifas", self.main_img)

    def tearDown(self):
        pass

    def test_add_item(self):
        BAG_MAX_SIZE = 20
        for i in range(BAG_MAX_SIZE):
            self.assertTrue(self.p.add_item(i))
        self.assertFalse(self.p.add_item(100))

    def test_take_item(self):
        self.p.add_item(1)
        self.assertFalse(self.p.take_item(2))
        self.assertTrue(self.p.take_item(1))
        self.assertFalse(self.p.take_item(1))

    def test_add_remove_pokemon(self):
        self.assertTrue(self.p.add_pokemon(1))
        self.assertTrue(self.p.add_pokemon(2))
        self.assertTrue(self.p.add_pokemon(3))
        self.assertTrue(self.p.add_pokemon(4))
        self.assertTrue(self.p.add_pokemon(5))
        self.assertTrue(self.p.add_pokemon(6))
        self.assertFalse(self.p.add_pokemon(0))
        self.assertTrue(self.p.take_pokemon(1))
        self.assertFalse(self.p.take_pokemon(1))
        self.assertTrue(self.p.take_pokemon(2))
        self.assertTrue(self.p.take_pokemon(3))
        self.assertTrue(self.p.take_pokemon(4))
        self.assertTrue(self.p.take_pokemon(6))
        self.assertTrue(self.p.take_pokemon(5))
        self.assertFalse(self.p.take_pokemon(1))

    def test_swap_pokemon(self):
        self.p.add_pokemon(1)
        self.p.add_pokemon(2)
        self.p.add_pokemon(3)
        self.assertTrue(self.p.swap_pokemon(1,2))
        self.assertFalse(self.p.swap_pokemon(1,4))

    def test_add_cracha(self):
        self.assertTrue(self.p.add_cracha("cracha1"))

    def test_movement(self):
        self.assertTrue(self.p.moveUp())
        self.assertTrue(self.p.moveRight())
        self.assertTrue(self.p.moveLeft())
        self.assertTrue(self.p.moveDown())


if __name__ == '__main__':
    unittest.main()
