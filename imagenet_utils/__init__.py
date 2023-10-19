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

def _deduplicate_nodes(nodes):
    i = 0
    while i < len(nodes):
        j = i + 1
        while j < len(nodes):
            if nodes[i] == nodes[j]:
                nodes.pop(j)
            else:
                j += 1
        i += 1
    return nodes

def name_to_node(name: str):
    result = _name_to_node(node=dict(id=None, names=["root"], children=METADATA), name=name, result=[])
    result = _deduplicate_nodes(result)
    if len(result) > 1:
        ids = ", ".join([node["id"] for node in result])
        raise ValueError(f"name '{name}' is not unique ({ids})")
    return result[0]

def _name_to_node(node, name: str, result):
    for i in range(len(node["names"])):
        if node["names"][i] == name:
            result.append(node)
    for child in node["children"]:
        _name_to_node(node=child, name=name, result=result)
    return result

def name_to_wordnetid(name: str) -> str:
    node = name_to_node(name)
    return node["id"]


def name_to_leafindices(name: str):
    wordnetid = name_to_wordnetid(name)
    return wordnetid_to_leafindices(wordnetid)

def get_all_nonleaf_wordnetids():
    nodes = _get_all_nonleaf_wordnetids(node=dict(id=None, names=["root"], children=METADATA), result=[])
    nodes = _deduplicate_nodes(nodes)
    return [node["id"] for node in nodes]

def _get_all_nonleaf_wordnetids(node, result):
    children = node["children"]
    if len(children) > 1 and node["id"] is not None:
        result.append(node)
    for child in children:
        _get_all_nonleaf_wordnetids(node=child, result=result)
    return result

def get_all_hierarchies():
    hierarchy_wordnetids = get_all_nonleaf_wordnetids()
    hierarchies = [wordnetid_to_leafindices(wordnetid) for wordnetid in hierarchy_wordnetids]
    # it is possible that a hierarchy has only 1 leafnode if it branches into two hierarchies that each have only 1
    # child and the child is equal to the child of the other hierarchy
    # example: n02760429: automatic firearm
    hierarchies = [hierarchy for hierarchy in hierarchies if len(hierarchy) > 1]
    return hierarchies