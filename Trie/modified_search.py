class TrieNode:
    def __init__(self):
        self.hmap = {}
        self.end_of_word = False
    
    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.hmap:
                curr.hmap[c] = TrieNode()
            curr = curr.hmap[c]
        curr.end_of_word = True
    
    def search(self, word):
        curr = self
        for c in word:
            if c not in curr.hmap:
                return False
            curr = curr.hmap[c]
        return curr.end_of_word

class Solution:
    def __init__(self):
        pass
    
    def modified_search(self, word):

        n = len(word)
        old_word = word
        word = list(word)
        for i in range(n):
            char = word[i]
            for j in range(ord('a'), ord('z')+1):
                word[i] = chr(j)
                if ''.join(word) == old_word:
                    continue
                print(''.join(word))
                word_present = self.root.search(word)
                if word_present:
                    return word_present
                else:
                    word[i] = char
        return False
                
        #     if word[i] in curr.hmap:
        #         curr = curr.hmap[word[i]]
        #     else:
        #         for key in curr.hmap:
        #             mod = 1
        #             print(key, end=' ')
        #             new_curr = curr.hmap[key]
        #             for j in range(i+1, n):
        #                 print(word[j], end=' ')
        #                 print(mod, end = ' ')
        #                 if word[j] in new_curr.hmap:
        #                     new_curr = new_curr.hmap[word[j]]
        #                 else:
        #                     mod = 2
        #                     break
        #             if mod == 1 and new_curr.end_of_word:
        #                 return '1'
        #         return '0'
        # return '0'

    def solve(self, A, B):
        self.root = TrieNode()
        for word in A:
            self.root.insert(word)
        ans = ''
        for word in B:
            ans += str(int(self.modified_search(word)))
        return ans

if __name__ == '__main__':

    sol = Solution()
    t = int(input())
    for _ in range(t):

        A = input()
        A = A.split()
        B = input()
        B = B.split()
        print(sol.solve(A, B))