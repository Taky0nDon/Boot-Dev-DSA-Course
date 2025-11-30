from typing import Optional
class Trie:
    def search_level(self, current_level: dict[str,str|bool],
                     current_prefix: str,
                     words: list[str]) -> Optional[list[str]]:
        if self.end_symbol in current_level:
            words.append(current_prefix)
        for char in sorted(current_level.keys()):
            if char != self.end_symbol:
                self.search_level(current_level[char], f"{current_prefix}{char}", words)
        return words

    def words_with_prefix(self, prefix: str) -> list[str]:
        matches = []
        current_level = self.root
        for char in prefix:
            current_level = current_level.get(char)
            if current_level is None:
                return matches
        return self.search_level(current_level, prefix, matches)

    def find_matches(self, document: str) -> set:
        matches = set()
        i = 0
        iters = 0
        while i < len(document):
            current_level = self.root
            j = i
            while j < len(document):
                iters += 1
                char = document[j]
                j += 1
                if char not in current_level:
                    break
                current_level = current_level[char]
                if self.end_symbol in current_level:
                    matches.add(document[i:j])
            i = j
        print(iters == len(document))
        return matches



    def exists(self, word: str) -> bool:
        current_level = self.root
        for char in word:
            if char not in current_level:
                return False
            current_level = current_level[char]
        return self.end_symbol in current_level

    def add(self, word: str) -> None:
        current_level = self.root
        for char in word:
            if char not in current_level:
                current_level[char] = {}
            current_level = current_level[char]
        current_level[self.end_symbol] = True

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

