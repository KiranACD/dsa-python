def main():

    tests = num_test_cases()
    for _ in range(tests):
        n, m = num_words_prefixes()
        print(n, m)
        words = get_words()
        print(words)
        weights = get_weights()
        print(weights)
        prefixes = get_prefixes()

def num_test_cases():
    n = input()
    return int(n)

def num_words_prefixes():
    num = input()
    num = list(map(int, num.split()))
    return num[0], num[1]

def get_words():
    words = input()
    words = words.split()
    return words

def get_weights():
    weights = input()
    weights = list(map(int, weights.split()))
    return weights

def get_prefixes():
    prefixes = input()
    prefixes = prefixes.split()
    return prefixes

if __name__ == '__main__':
    main()