import unittest

from imagenet_utils import *
from imagenet_utils.versions import IN13_FELINES_CLASSES


class TestInit(unittest.TestCase):
    def test_index_to_wordnetid(self):
        self.assertEqual("n01496331", index_to_wordnetid(5))

    def test_indices_to_wordnetids(self):
        self.assertEqual(["n01496331", "n02128385"], indices_to_wordnetids([5, 288]))

    def test_wordnetid_to_index(self):
        self.assertEqual(5, wordnetid_to_index("n01496331"))

    def test_wordnetid_to_index_identity(self):
        for i in range(1000):
            self.assertEqual(i, wordnetid_to_index(index_to_wordnetid(i)))

    def test_wordnetids_to_indices(self):
        self.assertEqual([5, 288], wordnetids_to_indices(["n01496331", "n02128385"]))

    def test_index_to_name(self):
        self.assertEqual(["leopard", "Panthera pardus"], index_to_names(288))

    def test_index_to_shortest_name(self):
        self.assertEqual("leopard", index_to_shortest_name(288))

    def test_wordnetid_to_shortest_name(self):
        self.assertEqual("leopard", wordnetid_to_shortest_name("n02128385"))

    def test_wordnetid_to_names(self):
        self.assertEqual(["leopard", "Panthera pardus"], wordnetid_to_names("n02128385"))

    def test_wordnetid_to_node(self):
        feline_node = wordnetid_to_node("n02120997")
        leafs = node_to_leafwordnetids(feline_node)
        self.assertEqual(IN13_FELINES_CLASSES, leafs)
        self.assertEqual(IN13_FELINES_CLASSES, wordnetid_to_leafwordnetids("n02120997"))

    def test_wordnetids_to_shortest_name(self):
        self.assertEqual(["torpedo", "leopard"], wordnetids_to_shortest_name(["n01496331", "n02128385"]))

    def test_wordnetid_to_leafnames(self):
        feline_leafnames = wordnetid_to_leafnames("n02120997")
        self.assertEqual(wordnetids_to_shortest_name(IN13_FELINES_CLASSES), feline_leafnames)

    def test_wordnetid_to_leafindices(self):
        feline_leafindices = wordnetid_to_leafindices("n02120997")
        self.assertEqual(wordnetids_to_indices(IN13_FELINES_CLASSES), feline_leafindices)

    def test_wordnetid_to_leafindices_no_duplicates(self):
        animal_wordnetid = name_to_wordnetid("animal")
        animal_leafindices = wordnetid_to_leafindices(animal_wordnetid)
        self.assertEqual(398, len(animal_leafindices))

    def test_name_to_node(self):
        feline_node = name_to_node("feline")
        leafs = node_to_leafwordnetids(feline_node)
        self.assertEqual(IN13_FELINES_CLASSES, leafs)

    def test_name_to_node_not_unique(self):
        with self.assertRaises(ValueError) as ex:
            name_to_node("car")
        self.assertEqual("name 'car' is not unique (n02959942, n02958343)", str(ex.exception))

    def test_name_to_wordnetid(self):
        self.assertEqual("n02120997", name_to_wordnetid("feline"))

    def test_name_to_leafindices(self):
        feline_leafindices = name_to_leafindices("feline")
        self.assertEqual(wordnetids_to_indices(IN13_FELINES_CLASSES), feline_leafindices)

    def test_in118_dogs(self):
        self.assertEqual(118, len(name_to_leafindices("dog")))

    def test_in13_feline(self):
        self.assertEqual(13, len(name_to_leafindices("feline")))

    def test_in158_carnivore(self):
        self.assertEqual(158, len(name_to_leafindices("carnivore")))

    def test_in218_mammal(self):
        self.assertEqual(218, len(name_to_leafindices("mammal")))

    def test_in337_vertebrate(self):
        self.assertEqual(337, len(name_to_leafindices("vertebrate")))

    def test_in398_animal(self):
        self.assertEqual(398, len(name_to_leafindices("animal")))

    def test_in59_bird(self):
        self.assertEqual(59, len(name_to_leafindices("bird")))

    def test_in36_reptile(self):
        self.assertEqual(36, len(name_to_leafindices("reptile")))

    def test_in61_invertebrate(self):
        self.assertEqual(61, len(name_to_leafindices("invertebrate")))

    def test_in7_fungus(self):
        self.assertEqual(7, len(name_to_leafindices("fungus")))

    def test_in26_musical_instrument(self):
        self.assertEqual(26, len(name_to_leafindices("musical instrument")))

    def test_in8_truck(self):
        self.assertEqual(8, len(name_to_leafindices("truck")))

    def test_in10_car(self):
        self.assertEqual(10, len(wordnetid_to_leafindices("n02958343")))

    def test_in22_motor_vehicle(self):
        self.assertEqual(22, len(name_to_leafindices("motor vehicle")))

    def test_in43_wheeled_vehicle(self):
        self.assertEqual(43, len(name_to_leafindices("wheeled vehicle")))

    def test_in10_ball(self):
        self.assertEqual(10, len(name_to_leafindices("ball")))

    def test_in49_clothing(self):
        self.assertEqual(49, len(name_to_leafindices("clothing")))

    def test_in8_shop(self):
        self.assertEqual(8, len(name_to_leafindices("shop")))

    def test_in57_structure(self):
        self.assertEqual(57, len(name_to_leafindices("structure")))
