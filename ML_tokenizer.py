from dataclasses import dataclass, field


@dataclass
class Node:
    children: dict[str, "Node"] = field(default_factory=dict)
    token_id: int = -1


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, token_word, token_id):
        curr = self.root
        for t in token_word:
            if t not in curr.children:
                curr.children[t] = Node()
            curr = curr.children[t]
        curr.token_id = token_id

    def encode(self, word):
        res = []
        i, n = 0, len(word)

        while i < n:
            curr_node = self.root

            tmp_token_id = -1
            for j in range(i, n):
                t = word[j]
                if t in curr_node.children:
                    curr_node = curr_node.children[t]

                    if curr_node.token_id != -1:
                        tmp_token_id = curr_node.token_id
                        i = j
                else:
                    break

            res.append(tmp_token_id)
            i += 1

        return res

    def print_tree(self):
        def print_tree_(node: Node, tab):
            for ch, child in node.children.items():
                print(tab * "\t", ch, child.token_id)
                print_tree_(child, tab + 1)

        print_tree_(self.root, 0)
