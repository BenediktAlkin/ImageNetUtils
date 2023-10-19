# parse data from https://gist.githubusercontent.com/mbostock/535395e279f5b83d732ea6e36932a9eb/raw/62863328f4841fce9452bc7e2f7b5e02b40f8f3d/mobilenet.json
import json


class Node:
    def __init__(self, wordnetid: str):
        self.wordnetid = wordnetid
        self.children = []


def create_tree(root_dict, level=0):
    if "children" in root_dict:
        print("\t" * level + "[")
        for child in root_dict["children"]:
            print("\t" * (level + 1) + "{")
            print("\t" * (level + 2) + f'"id": "{child["id"]}",')
            names = ", ".join([f'"{name}"' for name in child["name"].split(", ")])
            print("\t" * (level + 2) + f'"names": [{names}],')
            if "children" in child:
                print("\t" * (level + 2) + f'"children":')
                create_tree(root_dict=child, level=level + 2)
            else:
                print("\t" * (level + 2) + f'"children": [],')
            print("\t" * (level + 1) + "},")
        print("\t" * level + "],")


def main():
    with open("mobilenet.json") as f:
        data = json.load(f)
    create_tree(root_dict=data)


if __name__ == "__main__":
    main()
