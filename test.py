import unittest
from clas import *


class TestSeaBoat(unittest.TestCase):
    def test_valid_creation(self):
        boat = SeaBoat("Wave", 6, 200.0, 800.0, 2015)
        self.assertEqual(boat.name, "Wave")
        self.assertEqual(boat.passenger_capacity, 6)
        self.assertEqual(boat.engine_power, 200.0)
        self.assertEqual(boat.cargo_capacity, 800.0)
        self.assertEqual(boat.build_year, 2015)

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            SeaBoat("", 6, 200.0, 800.0, 2015)
        with self.assertRaises(ValueError):
            SeaBoat("   ", 6, 200.0, 800.0, 2015)
        with self.assertRaises(ValueError):
            SeaBoat(123, 6, 200.0, 800.0, 2015)

    def test_invalid_passenger_capacity(self):
        with self.assertRaises(ValueError):
            SeaBoat("Wave", -5, 200.0, 800.0, 2015)
        with self.assertRaises(ValueError):
            SeaBoat("Wave", 5.5, 200.0, 800.0, 2015)

    def test_invalid_engine_power(self):
        with self.assertRaises(ValueError):
            SeaBoat("Wave", 6, 0, 800.0, 2015)
        with self.assertRaises(ValueError):
            SeaBoat("Wave", 6, -150.0, 800.0, 2015)
        with self.assertRaises(ValueError):
            SeaBoat("Wave", 6, "Потужний", 800.0, 2015)

    def test_invalid_cargo_capacity(self):
        with self.assertRaises(ValueError):
            SeaBoat("Wave", 6, 200.0, -500.0, 2015)

    def test_invalid_build_year(self):
        current_year = 2026
        with self.assertRaises(ValueError):
            SeaBoat("Wave", 6, 200.0, 800.0, 1799)
        with self.assertRaises(ValueError):
            SeaBoat("Wave", 6, 200.0, 800.0, current_year + 1)
        with self.assertRaises(ValueError):
            SeaBoat("Wave", 6, 200.0, 800.0, "2015")

    def test_equality_method(self):
        boat1 = SeaBoat("Wave", 6, 200.0, 800.0, 2015)
        boat2 = SeaBoat("Wave", 6, 200.0, 800.0, 2015)
        boat3 = SeaBoat("Titan", 50, 1000.0, 5000.0, 2010)

        self.assertEqual(boat1, boat2)
        self.assertNotEqual(boat1, boat3)
        self.assertNotEqual(boat1, "Wave")

    def test_sorting_logic(self):
        b1 = SeaBoat("Catcher", 4, 150.0, 500.0, 2015)
        b2 = SeaBoat("Wave", 6, 200.0, 800.0, 2015)
        b3 = SeaBoat("Explorer", 12, 300.0, 1200.0, 2020)

        boats = [b1, b3, b2]
        boats.sort(key=lambda x: (x.build_year, -x.engine_power))
        self.assertEqual(boats[0].name, "Wave")
        self.assertEqual(boats[1].name, "Catcher")
        self.assertEqual(boats[2].name, "Explorer")


if __name__ == "__main__":
    unittest.main()