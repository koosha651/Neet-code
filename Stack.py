# NeetCode Challenge
# Solving Problems from NeetCode website, Stack


1. Valid Parentheses

def parentheses(s):
    stack = []
    closeToOpen = {']': '[', ')' : '(', '}' : '{'}

    for c in s:
        if c in closeToOpen:  # If the 'c' considers as closing character, because the keys in dictionary are closing character
            if stack and stack[-1] == closeToOpen[c]:     # if stack passed when stack was not empty, also it make sure at top of stack the 'c' maching the open parantheses
                stack.pop()
            else:
                return False

        else:              # only we append the opening parantheses charecter and move forward
            stack.append(c)

    return True if not stack else False         # if not stack = if stack was empty


s='}()[]'
parentheses(s)

output: False


#=============================================================================================================================================================================


2.  Min Stack

input: ["MinStack","push","push","push","getMin","pop","top","getMin"]
       [     []   , [-2] ,  [0] , [-3] ,   []   , []  , []  ,    []  ]

class MinStack:

    def __init__(self):
        self.stack = []   # make one stack for storing values
        self.minstack = []     # make one stack to store the minimum value on all numbers on the top of the stack

    def push(self, val: int) -> None:
        self.stack.append(val)
        val= min(val , self.minstack[-1] if self.minstack else val)   #update the stack/ choose between curent value and value in minstack
        self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


output:
[null,null,null,null,-3,null,0,-2]


#=============================================================================================================================================================================
