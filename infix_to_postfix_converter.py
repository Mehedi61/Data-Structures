# Programmed by MD. Mehedi Hasan

from pythonds.basic.stack import Stack

precedence = {}
precedence['*'] = 3
precedence['/'] = 3
precedence['+'] = 2
precedence['-'] = 2
precedence['('] = 1

def convert(expression):
    print(__convert(expression.split()))
    
def __convert(tokens):
    postfix = []
    opstack = Stack()
    
    for token in tokens:
        if token.isidentifier():
            postfix.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            while True:
                temp = opstack.pop()
                if temp is None or temp == '(':
                    break
                elif not temp.isidentifier():
                    postfix.append(temp)
            
        else: # must be operator
            if not opstack.isEmpty():
                temp = opstack.peek()
            
                while not opstack.isEmpty() and precedence[temp] >= precedence[token] and token.isidentifier():
                    postfix.append(opstack.pop())
                    temp = opstack.peek()
                
            opstack.push(token)
                
    while not opstack.isEmpty():
        postfix.append(opstack.pop())
            
    return postfix
            
    
convert("A + B")
convert("A + B * C")
convert("A * ( B + C ) + D")

