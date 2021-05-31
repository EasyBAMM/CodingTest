# https://programmers.co.kr/learn/courses/30/lessons/60060?language=python3
# https://www.youtube.com/watch?v=OPNmxpeNL1o
class Trie:
    def __init__(self):
        self.child = dict()
        self.count = 0

    def insert(self, str):
        curr = self
        for ch in str:   # go leaf node
            curr.count += 1
            if ch not in curr.child:
                curr.child[ch] = Trie()

            curr = curr.child[ch]
        curr.count += 1

    def search(self, str):
        curr = self
        for ch in str:
            if ch == '?':
                return curr.count
            if ch not in curr.child:
                return 0
            curr = curr.child[ch]
        return curr.count


def solution(words, queries):
    TrieRoot = [Trie() for _ in range(10000)]
    ReTriRoot = [Trie() for _ in range(10000)]
    answer = []

    for str in words:
        TrieRoot[len(str) - 1].insert(str)
        ReTriRoot[len(str) - 1].insert(str[::-1])

    for str in queries:
        if str[0] != '?':
            answer.append(TrieRoot[len(str) - 1].search(str))
        else:
            answer.append(ReTriRoot[len(str) - 1].search(str[::-1]))

    return answer


'''
import re


def solution(words, queries):
    answer = []

    for pattern in queries:
        pattern = pattern.replace('?', '.')
        # pattern = ['.' if x == '?' else x for x in pattern]
        # pattern = ''.join(pattern)
        pattern += "$"
        # print("pattern: ", pattern)
        count = 0
        for word in words:
            if re.match(pattern, word) != None:
                count += 1
                # print("match: ", word)
            # else:
                # print("nonmatch: ", word)
        answer.append(count)
    # print(answer)
    return answer
'''
