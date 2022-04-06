# Given a string, remove every pair of conscutive duplicates until there are no...
# ...consecutive duplicates

s = input('Enter string')

n = len(s)
stack = []
top = -1
for _ in range(n):
    if top == -1:
        stack.append(s[_])
        top += 1
        continue
    
    if s[_] == stack[top]:
        stack = stack[:-1]
        top -= 1
    else:
        stack.append(s[_])
        top += 1
    
print(''.join(stack))

