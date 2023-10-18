import unittest
from imagenet_utils import index_to_wordnetid, wordnetid_to_index, wordnetid_to_node, node_to_leafwordnetids
from imagenet_utils.versions import IN13_FELINES_CLASSES

class TestInit(unittest.TestCase):
    def test_index_to_wordnetid(self):
        self.assertEqual("n01496331", index_to_wordnetid(5))
        self.assertEqual(5, wordnetid_to_index("n01496331"))
        for i in range(1000):
            self.assertEqual(i, wordnetid_to_index(index_to_wordnetid(i)))

    def test_wordnetid_to_node(self):
        feline_node = wordnetid_to_node("n02120997")
        leafs = node_to_leafwordnetids(feline_node)
        self.assertEqual(IN13_FELINES_CLASSES, leafs)
