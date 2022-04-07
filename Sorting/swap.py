def swap_num(a, b):

    a = a^b
    b = a^b
    a = a^b
    
    return a, b