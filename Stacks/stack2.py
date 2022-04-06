# Given 2 sorted stacks. Merge them in sorted order

class LL:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_stack(stack, top):

    new_stack = []
    new_top = -1
    while (top != -1):
        new_stack.append(stack[top])
        top -= 1
        new_top += 1
    return new_stack

def merge_stacks(s1, top1, s2, top2):

    new_stack = []
    new_top = -1
    while(top1 != -1 and top2 != -1):
        if s1[top1] > s2[top2]:
            new_stack.append(s1[top1])
            top1 -= 1
        else:
            new_stack.append(s2[top2])
            top2 -= 1
        new_top += 1
    
    while(top1 != -1):
        new_stack.append(s1[top1])
        top1 -= 1
        new_top += 1
    
    while(top2 != -1):
        new_stack.append(s2[top2])
        top2 -= 1
        new_top += 1
    
    new_stack = reverse_stack(new_stack, new_top)

    return list(map(lambda x: str(x), new_stack))

if __name__ == '__main__':

    s1 = input('Enter sorted stack as a string')
    top1 = len(s1) - 1
    s2 = input('Enter sorted stack as a string')
    top2 = len(s2) - 1

    print(' '.join(merge_stacks(s1, top1, s2, top2)))