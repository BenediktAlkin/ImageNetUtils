from .metadata import METADATA
from .versions.in1k import CLASSES as IN1K_CLASSES


def index_to_wordnetid(index: int) -> str:
    return IN1K_CLASSES[index]


def indices_to_wordnetids(indices):
    return [index_to_wordnetid(index) for index in indices]


def wordnetid_to_index(wordnetid: str) -> int:
    return IN1K_CLASSES.index(wordnetid)


def wordnetids_to_indices(wordnetids):
    return [wordnetid_to_index(wordnetid) for wordnetid in wordnetids]


def index_to_names(index: int):
    wordnetid = index_to_wordnetid(index)
    return wordnetid_to_names(wordnetid)


def wordnetid_to_names(wordnetid: str):
    node = wordnetid_to_node(wordnetid)
    return node["names"]


def wordnetid_to_node(wordnetid: str):
    return _wordnetid_to_node(node=dict(id=None, names=["root"], children=METADATA), wordnetid=wordnetid)


def _wordnetid_to_node(node, wordnetid: str):
    if node["id"] == wordnetid:
        return node
    for child in node["children"]:
        result = _wordnetid_to_node(node=child, wordnetid=wordnetid)
        if result is not None:
            return result
    return None


def index_to_shortest_name(index: int) -> str:
    wordnetid = index_to_wordnetid(index)
    return wordnetid_to_shortest_name(wordnetid)


def wordnetid_to_shortest_name(wordnetid: str) -> str:
    min_len = float("inf")
    min_name = None
    for name in wordnetid_to_names(wordnetid):
        if len(name) < min_len:
            min_len = len(name)
            min_name = name
    return min_name

def wordnetids_to_shortest_name(wordnetids):
    return [wordnetid_to_shortest_name(wordnetid) for wordnetid in wordnetids]


def node_to_leafwordnetids(node):
    result = _node_to_leafwordnetids(node=node, result=[])
    return list(sorted(set(result)))


def _node_to_leafwordnetids(node, result):
    children = node["children"]
    if len(children) == 0:
        result.append(node["id"])
        return result
    for child in children:
        _node_to_leafwordnetids(node=child, result=result)
    return result


def wordnetid_to_leafwordnetids(wordnetid: str):
    node = wordnetid_to_node(wordnetid)
    return node_to_leafwordnetids(node)


def wordnetid_to_leafnames(wordnetid: str):
    leafwordnetids = wordnetid_to_leafwordnetids(wordnetid)
    return [wordnetid_to_shortest_name(leafwordnetid) for leafwordnetid in leafwordnetids]


def wordnetid_to_leafindices(wordnetid: str):
    leafwordnetids = wordnetid_to_leafwordnetids(wordnetid)
    return [wordnetid_to_index(leafwordnetid) for leafwordnetid in leafwordnetids]


def name_to_node(name: str):
    return _name_to_node(node=dict(id=None, names=["root"], children=METADATA), name=name)

def _name_to_node(node, name: str):
    for i in range(len(node["names"])):
        if node["names"][i] == name:
            return node
    for child in node["children"]:
        result = _name_to_node(node=child, name=name)
        if result is not None:
            return result
    return None

def name_to_wordnetid(name: str) -> str:
    node = name_to_node(name)
    return node["id"]

def name_to_leafindices(name: str):
    wordnetid = name_to_wordnetid(name)
    return wordnetid_to_leafindices(wordnetid)