import unittest
import Pokemon


class TestPokemon(unittest.TestCase):
    def setUp(self):
        self.pokemon = Pokemon.Pokemon(name="Pikachu", type="Electric", level=5, nature="calm", gender="male", attacks=["Thundershock", "Tail Whip"])

    def tearDown(self):
        pass

    def test_add_atack(self):
        self.assertTrue(self.pokemon.add_attack("Tackle"))
        self.assertTrue(self.pokemon.add_attack("Growl"))
        self.assertFalse(self.pokemon.add_attack("Thunder"))

    def test_remove_attack(self):
        self.assertFalse(self.pokemon.remove_attack("Thunder"))
        self.assertTrue(self.pokemon.remove_attack("Tail Whip"))
        self.assertFalse(self.pokemon.remove_attack("Thundershock"))

    def test_rename(self):
        self.assertTrue(self.pokemon.rename("pika"))
        self.assertFalse(self.pokemon.rename(" "))


class TestAttack(unittest.TestCase):
    def setUp(self):
        self.thunder = Pokemon.Attack("Thunder", 100, 5)
        self.hyper_beam = Pokemon.Attack("Hyper Beam",120 ,5)
    def tearDown(self):
        pass

    def test_use_attack(self):
        self.assertEqual(self.thunder.use_attack(),100)
        self.assertEqual(self.hyper_beam.use_attack(), 120)
        self.assertEqual(self.hyper_beam.use_attack(), 120)
        self.assertEqual(self.hyper_beam.use_attack(), 120)
        self.assertEqual(self.hyper_beam.use_attack(), 120)
        self.assertEqual(self.hyper_beam.use_attack(), 120)
        self.assertEqual(self.hyper_beam.use_attack(), 0)        #return false or 0??

    def test_restore_attack(self):
        pass


if __name__ == '__main__':
    unittest.main()


