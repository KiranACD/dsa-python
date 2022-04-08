def enter_array():

    arr = input('Enter arr elements seperated by ",": ')
    arr.replace(' ', '')
    arr = arr.split(',')
    arr = list(map(lambda x: int(x), arr))

    return arr

if __name__ == '__main__':
    pass