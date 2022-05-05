# Trie

```
class TrieNode:
    def __init__(self):
        self.hmap = dict()
        self.is_end = False
```

## Insertion

- Consider these words: abc, abde, abcd, aab, glo, glow
- We are going to insert 'abc' first. There is a root node. Check if 'a' is present in the hash map of the root node. If present, go to the value of the key, else insert the character as key and map a new empty TrieNode to the key.
- Then move to the next character in the string and the next node. Check if 'b' is in the hashmap of the curent node. If present, go to the value of the key, else insert the character as key and map a new empty TrieNode to the key.
- Repeat the process until the first word is done. When the word is done, go to the last TrieNode which will have a empty hashmap and change the is_end boolean to True to indicate the end of the word.
- Go to the next word 'abde'. Start with the first character 'a' and the root node and the repeat the above process till the word is done and the is_end boolean is changed to True
- Repeat the above process till the all the words are done.
```
def insert(word):
    curr = root
    for c in word:
        if c not in curr.hmap:
            curr.hmap[c] = TrieNode
        curr = curr.hmap[c]
    curr.is_end = True
```
TC: O(N)
SC: O(N)

## Searching

- Say we want to search for aab.
- Start from the root node. Check if 'a' is present in the root node. In this case, it is present. 
- Then go to the value of the key 'a'. Check if the next character 'a' is present in the hashmap of the node. If present, go to the value of the key.
- Check if the third char 'b' is present in the hashmap. If present, go to the value of the key.
- As the word is done, check if the is_end boolean is True. If yes, then aab is present.
- If the word is not present, the search would have ended at any one of the above steps, as either the character will not be present in a hashmap or the is_end boolean will be False, even if all the characters of the word are present.
```
def search(word):
    curr = root
    for c in word:
        if c not in curr.hmap:
            return False
    return curr.is_end
```
TC: O(N)
SC: O(1)

