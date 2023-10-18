from .metadata import CLASS_NAMES, CLASS_HIERARCHY
from .versions.in1k import CLASSES as IN1K_CLASSES


def index_to_wordnetid(index: int) -> str:
    return IN1K_CLASSES[index]


def wordnetid_to_index(wordnetid: str) -> int:
    return IN1K_CLASSES.index(wordnetid)


def index_to_names(index: int):
    return CLASS_NAMES[index]


def wordnetid_to_names(wordnetid: str):
    index = wordnetid_to_index(wordnetid)
    return index_to_names(index)


def index_to_shortest_name(index: int) -> str:
    min_len = float("inf")
    min_name = None
    for name in CLASS_NAMES[index]:
        if len(name) < min_len:
            min_len = len(name)
            min_name = name
    return min_name


def wordnetid_to_shortest_name(wordnetid: str) -> str:
    index = wordnetid_to_index(wordnetid)
    return index_to_shortest_name(index)


def wordnetid_to_node(wordnetid: str):
    stack = [node for node in CLASS_HIERARCHY]
    while len(stack) > 0:
        node = stack.pop()
        if node["id"] == wordnetid:
            return node
        if len(node["children"]) > 0:
            stack += node["children"]
    raise ValueError(f"WordNet id '{wordnetid}' was not found in hierarchy")


def node_to_leafwordnetids(node):
    result = _node_to_leafwordnetids(node=node, result=[])
    return list(sorted(result))


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