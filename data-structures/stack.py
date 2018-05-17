# Programmed by MD. Mehedi Hasan

my_stack = []
print("\nCurrent Stack: " + str(my_stack))
print("The number of items on the stack: " + str(len(my_stack)) + "\n")

# push some items to the stack
my_stack.append('A')
my_stack.append('B')
my_stack.append('C')
my_stack.append('D')
my_stack.append('E')

print("Current Stack afer pushing some items: " + str((my_stack)))
print("The number of items on the stack: " + str(len(my_stack)) + "\n")

# pop an item form the stack
my_stack.pop()
print("Current Stack after poping an item: " + str(my_stack))
print("The number of items on the stack: " + str(len(my_stack)) + "\n")

# peek an item form the stack
peek = len(my_stack) - 1
print("Peeked item: " + my_stack[peek])
print("Current stack after peeking an item: " + str(my_stack))
print("The number of items on the stack: " + str(len(my_stack)) + "\n")
