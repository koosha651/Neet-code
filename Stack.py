# NeetCode Challenge
# Solving Problems from NeetCode website, Stack


1. Valid Parentheses

def parentheses(s):
    stack = []
    closeToOpen = {']': '[', ')' : '(', '}' : '{'}      # the keys in our map are closing parantheses we need to make sure if the stack is not empty

    for c in s:
        if c in closeToOpen:  # If the 'c' considers as closing character, because the keys in dictionary are closing character (it is only check 'c' with the dict keys)
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
        val= min(val , self.minstack[-1] if self.minstack else val)   #update the min value in minstack/ choose between min of value and top of stack, if the stack is non 
                                                                      # empty. If it is empty, we take the min of val and val
        self.minstack.append(val)       # if minstack is emptywe append the value to it 

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

3. Evaluate Reverse Polish Notation

# As we read through the list, pop() each value and add it to the Stack. If we reach to an operator, the two previous number is going to remove from Stack and we are going
# to do the operator on them, and then add the result to Stack

# ** for the '/' and '-' it is important to replace their position at First and then do the operation on them.

def evalRPN(tokens) -> int:
    stack=[]

    for i in tokens:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '-':
            a, b = stack.pop() , stack.pop()
            stack.append(b-a)
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == '/':
            a, b = stack.pop() , stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(i))                    # if the charecter was not a operator, it will be a number which first convert it to intiger and append it to Stack
    return stack[0]



#=============================================================================================================================================================================
