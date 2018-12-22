from stack import Stack

def parChecker(word):

    s = Stack()
    balanced = True

    for i in word:
        if i == '(':
            s.push(i)
        elif not s.isEmpty() and i == ')':
            s.pop()
        else:
            balanced = False
    
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('(((((())))))'))
print(parChecker('(()())))()))('))
