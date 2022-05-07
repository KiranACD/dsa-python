
def min_string_window(A, B):

    n = len(A)
    b_dict = {}
    for c in B:
        if c in b_dict:
            b_dict[c] += 1
        else:
            b_dict[c] = 1
    
    print(b_dict)
    a_dict = {}
    posn_dict = {}
    i = 0
    for c in A:
        if c in b_dict:
            if c in a_dict:
                if a_dict[c] < b_dict[c]:
                    a_dict[c] += 1
                    posn_dict[c].append(i)
            else:
                a_dict[c] = 1
                posn_dict[c] = [i]
        i += 1
    print(a_dict)
    print(posn_dict)
    s = n
    e = 0
    for key in b_dict:
        if key in a_dict:
            if a_dict[key] >= b_dict[key]:
                p = b_dict[key] - 1                
                s = min(posn_dict[key][0], s)
                e = max(posn_dict[key][p], e)
            else:
                return ''
        else:
            return ''
    return s, e

if __name__ == '__main__':
    A = input()
    B = input()
    print(min_string_window(A, B))

