from dataclasses import dataclass, field
from typing import List

DICTIONARY = {
    "ABACUS": ["AE", "B", "AH", "K", "AH", "S"],
    "BOOK": ["B", "UH", "K"],
    "BOAT": ["B", "O", "UH", "T"],
    "THEIR": ["DH", "EH", "R"],
    "THERE": ["DH", "EH", "R"],
    "TOMATO": ["T", "AH", "M", "AA", "T", "OW"],
    "TOMATO": ["T", "AH", "M", "EY", "T", "OW"],
}

"""
-> B -> UH -> K
     -> O -> UH -> T

-> DH -> EH -> R
"""


@dataclass
class Node:
    children: dict[str, "Node"] = field(default_factory=dict)
    words: List[str] = field(default_factory=list)


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word, phenomes: List[str]):
        curr = self.root
        for ph in phenomes:
            if ph not in curr.children:
                curr.children[ph] = Node()
            curr = curr.children[ph]
        curr.words.append(word)

    def search(self, phenomes: List[str]):
        curr = self.root
        for ph in phenomes:
            if ph not in curr.children:
                break
            curr = curr.children[ph]
        return curr.words

    def print(self):
        def _print(node, tab=0):
            for k, n in node.children.items():
                print("\t" * tab, k, "-- words:", n.words)
                _print(n, tab + 1)

        _print(self.root, 0)


t = Trie()
for word in DICTIONARY:
    t.add(word, DICTIONARY[word])
t.print()

result = t.search(["DH", "EH", "R"])
print(result)

result = t.search(["T", "AH", "M", "EY", "T", "OW"])
print(result)
