
def longestsubstring(A):
    
    s = 0
    e = 0
    d = {}
    n = len(A)
    i = 0
    max_len = 0

    while i < n:
        print(i)
        print(A[i])
        print(d)
        if A[i] in d:
            # print(i)
            print('here')
            i = d[A[i]]+1
            s = i
            e = i
            d.clear()
            d[A[i]] = i
        else:
            d[A[i]] = i
            e = i
        if (e-s+1) > max_len:
            max_len = e-s+1
        i += 1
        print('---------------------------------')
    return max_len

if __name__== "__main__":
    string = input()
    print(longestsubstring(string))