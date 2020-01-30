#Recursion
Structure: Base cases + recur if not base case
Tail recursion: When the last call in the function is a purely recursive call. hanoi.py has tail recursion while factorial.py doesn't. Tail recursion is an example of linear recursion since you can't make subsequent calls without finishing the current one first.
Pro: Exploits repetitive structure of programs and can often avoid nested loops
Con: The Python interpreter has to keep track of the state of the nested call, and this can take up some memory. 
