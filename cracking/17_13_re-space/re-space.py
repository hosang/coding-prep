#!/usr/bin/env python3


class Node(object):
    def __init__(self):
        self.is_end = False
        self.children = {}


class PostfixTree(object):
    def __init__(self, words):
        self._head = Node()
        for w in words:
            self.insert(w)

    def insert(self, word):
        p = self._head
        for c in word[::-1]:
            if c not in p.children:
                p.children[c] = Node()
            p = p.children[c]
        p.is_end = True

    def matched_lengths(self, word):
        p = self._head
        for length, c in enumerate(word[::-1], start=1):
            if c not in p.children:
                return
            else:
                p = p.children[c]
            if p.is_end:
                yield length


def respace(text, dictionary):
    pt = PostfixTree(dictionary)
    unrec = [0] * (len(text) + 1)
    bt = [(-1, -1)] * (len(text) + 1)
    for i, _ in enumerate(text):
        unrec[i + 1] = unrec[i] + 1
        bt[i + 1] = (i, False)
        for l in pt.matched_lengths(text[:i + 1]):
            prev = i + 1 - l
            if unrec[prev] < unrec[i + 1]:
                unrec[i + 1] = unrec[prev]
                bt[i + 1] = (prev, True)

    result = []
    p = len(text)
    while p > -1:
        start, match = bt[p]
        if match:
            result.append(text[start:p])
        else:
            result.append(text[start:p] + '*')
        p = start
    return ' '.join(result[::-1])


if __name__ == '__main__':
    text = respace('jesslookedjustliketimherbrother',
                   ['looked', 'just', 'like', 'her', 'brother'])
    print(text)
