# Stacks

This implementation of stacks uses the adapter design pattern wherein an existing class (python's lists in this case) are modified to function like a stack in a more convenient manner

When a stack is empty and you try to pop an element off the stack, it can't be an IndexError because stacks don't have indices. Instead you'd define a class of error called 'Empty'

