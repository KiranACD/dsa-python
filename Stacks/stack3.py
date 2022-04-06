# Given a stack, sort it in descending order

import sys
sys.setrecursionlimit(10**3)

def reverse_stack(stack, top):

    reverse_stack = []
    reverse_top = -1

    while (top != -1):
        reverse_stack.append(stack[top])
        top -= 1
        reverse_top += 1
    
    return reverse_stack, reverse_top

def merge_stacks(s1, top1, s2, top2):
    
    new_stack = []
    new_top = -1

    while(top1 != -1 and top2 != -1):
        if s1[top1] < s2[top2]:
            new_stack.append(s1[top1])
            top1 -= 1
        else:
            new_stack.append(s2[top2])
            top2 -= 1
        new_top += 1
    
    while (top1 != -1):
        new_stack.append(s1[top1])
        top1 -= 1
        new_top += 1
    
    while(top2 != -1):
        new_stack.append(s2[top2])
        top2 -= 1
        new_top += 1
    
    new_stack, new_top = reverse_stack(new_stack, new_top)
    
    return new_stack, new_top

def merge_sort(stack, top):

    if len(stack) <= 1:
        return stack, top

    half_stack = []
    half_top = -1

    n = len(stack)

    for _ in range(n//2):
        half_stack.append(stack[top])
        stack.pop(top)
        half_top += 1   
        top -= 1
    
    s2, top2 = merge_sort(half_stack, half_top)
    s1, top1 = merge_sort(stack, top)

    print('stack1 = {0}, stack2 = {1}, top1 = {2}, top2 = {3}'.format(s1, s2, top1, top2))
    return merge_stacks(s1, top1, s2, top2)


def implement_merge_sort():

    s = input('Enter the stack as a string: ')
    n = len(s)

    s = list(map(lambda x: int(x), s))

    return merge_sort(s, n-1)

if __name__ == '__main__':
    print(implement_merge_sort())


